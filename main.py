import tkinter
from userAction import *
from productAction import *
from grader import *


def mycart():
    global session
    win_cart = tkinter.Toplevel(win)
    win_cart.geometry('400x300')
    win_cart.title('My Cart')

    result = getUserCart(session)

    lstbx_cart= tkinter.Listbox(win_cart, width=60)
    lstbx_cart.pack()
    for product in result:
        text = f"Name: {product[1]},   QNT: {product[0]},   Total Price: {product[0] * product[2]}"
        lstbx_cart.insert('end', text)

    win_cart.mainloop()


def shop ():

    def buy():
        global session
        pid = txt_id.get()
        qnt = txt_qnt.get()
        result, msg = shopValidate(pid, qnt)
        if not result:
            lbl_msg_shop.configure(text=msg, fg='red')
            return
        savetocart(session, pid, qnt)
        updateqnt(pid, qnt)
        lstbx.delete(0, 'end')
        products = getAllProducts()
        for product in products:
            text = f"id: {product[0]},  name: {product[1]},  price: {product[2]},  quantity: {product[3]}"
            lstbx.insert('end', text)
        
        lbl_msg_shop.configure(text='Saved to Your Cart!', fg='green')
        txt_id.delete(0, 'end')
        txt_qnt.delete(0, 'end')
        

        

    
    win_shop = tkinter.Toplevel(win)
    win_shop.geometry('400x300')
    win_shop.title('Available Products')

    products = getAllProducts()
    lstbx = tkinter.Listbox(win_shop, width=60)
    lstbx.pack()

    for product in products:
        text = f"ID: {product[0]},     Name: {product[1]},    Price: {product[2]},   Quantity: {product[3]}"
        lstbx.insert('end', text)

    lbl_id = tkinter.Label(win_shop, text='Product ID:')
    lbl_id.pack()
    txt_id = tkinter.Entry(win_shop)
    txt_id.pack()

    lbl_qnt = tkinter.Label(win_shop, text='QNT:')
    lbl_qnt.pack()
    txt_qnt = tkinter.Entry(win_shop)
    txt_qnt.pack()

    lbl_msg_shop = tkinter.Label(win_shop, text='')
    lbl_msg_shop.pack()

    btn_buy = tkinter.Button(win_shop, text='Buy!', command = buy)
    btn_buy.pack()
    
    
    win_shop.mainloop()

def login ():
    global session
    user = txt_user.get()
    pas = txt_pass.get()
    result = user_login(user, pas)
    if result:
        session, u_name = result
        lbl_msg.configure(text=f"Welcome to Your Account, {u_name}!", fg="green")
        txt_user.delete(0, "end")
        txt_pass.delete(0, "end")
        grade = check_grade(u_name)
        btn_login.configure(state="disabled")
        btn_logout.configure(state='active')

        if btn_shop.cget('text') in grade:
            btn_shop.configure(state='active')

        if btn_cart.cget('text') in grade:
            btn_cart.configure(state='active')

        if btn_admin.cget('text') in grade:
            btn_admin.configure(state='active')



    else:
        lbl_msg.configure(text="Wrong username / password", fg="red")

def logout():
    global session
    btn_login.configure(state="active")
    btn_logout.configure(state="disabled")
    btn_shop.configure(state='disabled')
    btn_cart.configure(state='disabled')
    btn_admin.configure(state='disabled')
    lbl_msg.configure(text='U R Out!', fg='blue')
    session = False
    


def submit():

    def register ():
        user = txt_user.get()
        pas = txt_pass.get()
        address = txt_addr.get()
        result, msg = user_submit(user, pas, address)
        if result:
            lbl_msg.configure(text="Submit Done!", fg = "green")
            txt_user.delete(0, 'end')
            txt_pass.delete(0, 'end')
            txt_addr.delete(0, 'end')
            btn_submit.configure(state="disabled")
        else:
            lbl_msg.configure(text=msg, fg="red")

        
    
    win_submit = tkinter.Toplevel()
    win_submit.title("Submit Panel")
    win_submit.geometry("300x400")

    lbl_user = tkinter.Label(win_submit, text="Username:")
    lbl_user.pack()
    txt_user = tkinter.Entry(win_submit)
    txt_user.pack()


    lbl_pass = tkinter.Label(win_submit, text="Password:")
    lbl_pass.pack()
    txt_pass = tkinter.Entry(win_submit)
    txt_pass.pack()

    lbl_addr = tkinter.Label(win_submit, text="Address:")
    lbl_addr.pack()
    txt_addr = tkinter.Entry(win_submit)
    txt_addr.pack()


    lbl_msg = tkinter.Label(win_submit, text = "")
    lbl_msg.pack()


    btn_submit = tkinter.Button(win_submit, text="Submit", command=register)
    btn_submit.pack()

    
    
    win_submit.mainloop()



# ------------------------------------------ Update Quantity ------------------------------------------
def admin():

    def deincrement():

        def upt_qnt():
            id = txt_update_id.get()
            qnt = txt_update_qnt.get()
            status, msg, color = updateQNT(id, qnt)
            if status:
                txt_update_qnt.delete(0, 'end')
                txt_update_id.delete(0, 'end')
                lstbx.delete(0, 'end')
                products = getAllProducts()

                for product in products:
                    text = f"ID: {product[0]},   Name: {product[1]},   Price: {product[2]},   Quantity: {product[3]}"
                    lstbx.insert('end', text)
                lbl_msg_update.configure(text=msg, fg=color)
            else:
                lbl_msg_update.configure(text=msg, fg=color)

        dein = tkinter.Toplevel(win_admin)
        dein.geometry('400x320')
        dein.title("Update Quantities")

        lbl_update_product = tkinter.Label(dein, text='In Stock Items:')
        lbl_update_product.pack()

        products = getAllProducts()
        lstbx = tkinter.Listbox(dein, width=60)
        lstbx.pack()

        for product in products:
            text = f"ID: {product[0]},   Name: {product[1]},   Price: {product[2]},   Quantity: {product[3]}"
            lstbx.insert('end', text)

        lbl_update_id = tkinter.Label(dein, text='Product ID')
        lbl_update_id.pack()
        txt_update_id = tkinter.Entry(dein)
        txt_update_id.pack()

        lbl_update_qnt = tkinter.Label(dein, text='Product New Quantity')
        lbl_update_qnt.pack()
        txt_update_qnt = tkinter.Entry(dein)
        txt_update_qnt.pack()

        lbl_msg_update = tkinter.Label(dein, text='')
        lbl_msg_update.pack()

        btn_update = tkinter.Button(dein, text='Update Product Quantity', command=upt_qnt)
        btn_update.pack()

        dein.mainloop()




# ----------------------------------------------- Add new Products -----------------------------------------------

    def add_product():
        def addP():
            pname = txt_add_name.get()
            price = txt_add_price.get()
            qnt = txt_add_qnt.get()
            a, msg = addProduct(pname, price, qnt)
            if a:
                lstbx.delete(0, 'end')
                products = getAllProducts()

                for product in products:
                    text = f"ID: {product[0]},  Name: {product[1]},  Price: {product[2]},  Quantity: {product[3]}"
                    lstbx.insert('end', text)
                txt_add_price.delete(0, 'end')
                txt_add_qnt.delete(0, 'end')
                txt_add_name.delete(0, 'end')
                lbl_msg_add.configure(text = 'The New Product Added Successfully', fg='green')
            else:
                lbl_msg_add.configure(text=msg, fg='red')


        win_add = tkinter.Toplevel(win_admin)
        win_add.title('Add New Product')
        win_add.geometry('400x360')

        lbl_add_product1 = tkinter.Label(win_add, text='In Stock Items:')
        lbl_add_product1.pack()

        products = getAllProducts()
        lstbx = tkinter.Listbox(win_add, width=60)
        lstbx.pack()

        for product in products:
            text = f"ID: {product[0]},  Name: {product[1]},  Price: {product[2]},  Quantity: {product[3]}"
            lstbx.insert('end', text)


        lbl_add_name = tkinter.Label(win_add, text='New Product Name')
        lbl_add_name.pack()
        txt_add_name = tkinter.Entry(win_add)
        txt_add_name.pack()

        lbl_add_price = tkinter.Label(win_add, text='New Product Price')
        lbl_add_price.pack()
        txt_add_price = tkinter.Entry(win_add)
        txt_add_price.pack()

        lbl_add_qnt = tkinter.Label(win_add, text='New Product Quantity')
        lbl_add_qnt.pack()
        txt_add_qnt = tkinter.Entry(win_add)
        txt_add_qnt.pack()

        lbl_msg_add = tkinter.Label(win_add, text="")
        lbl_msg_add.pack()

        btn_add_new_product = tkinter.Button(win_add, text='Add Product', command=addP)
        btn_add_new_product.pack()

        win_add.mainloop()




    # ----------------------------------------------- USER Manager -----------------------------------------------

    def user_manager():

        def updatePermissions():
            id = txt_user_id.get()
            grade = txt_user_permission.get()

            uptResult, uptmsg = updateUserPermissions(id, grade)

            if not uptResult:
                lbl_msg_usr_pr.configure(text=uptmsg, fg='red')

            if uptResult:
                txt_user_permission.delete(0, 'end')
                txt_user_id.delete(0, 'end')
                lsbx_users.delete(0, 'end')
                lbl_msg_usr_pr.configure(text=uptmsg, fg='green')

                result_users, rows = getAllUsers()

                if not result_users:
                    lbl_msg_usr_pr.configure(text=rows, fg='red')

                if result_users:
                    for row in rows:
                        text = f"ID:  {row[0]}   .:.   Username: {row[1]}   ->   Grade: {row[4]}"
                        lsbx_users.insert('end', text)




        win_uManager = tkinter.Toplevel(win_admin)
        win_uManager.title('User Manager')
        win_uManager.geometry('300x380')

        result, dic = userSetting()

        lbl_title_uManager = tkinter.Label(win_uManager, text='Permissions')
        lbl_title_uManager.pack()

        lsbx_permissions = tkinter.Listbox(win_uManager, width=45, height=6)
        lsbx_permissions.pack()

        lbl_usr_list = tkinter.Label(win_uManager, text="All Users")
        lbl_usr_list.pack()

        lsbx_users = tkinter.Listbox(win_uManager, width=45, height=6)
        lsbx_users.pack()

        lbl_user_id = tkinter.Label(win_uManager, text='User ID')
        lbl_user_id.pack()
        txt_user_id = tkinter.Entry(win_uManager)
        txt_user_id.pack()

        lbl_user_permission = tkinter.Label(win_uManager, text='User Permission')
        lbl_user_permission.pack()
        txt_user_permission = tkinter.Entry(win_uManager)
        txt_user_permission.pack()

        lbl_msg_usr_pr = tkinter.Label(win_uManager, text='')
        lbl_msg_usr_pr.pack()

        btn_user_permission = tkinter.Button(win_uManager, text='Update Permissions', command=updatePermissions)
        btn_user_permission.pack()


        if not result:
            lbl_msg_usr_pr.configure(text=dic, fg='red')

        if result:
            for key, value in dic.items():
                text = f"Grade {key} -> {value}"
                lsbx_permissions.insert('end', text)

        result_users, rows = getAllUsers()

        if not result_users:
            lbl_msg_usr_pr.configure(text=rows, fg='red')

        if result_users:
            for row in rows:
                text = f"ID:  {row[0]}   .:.   Username: {row[1]}   ->   Grade: {row[4]}"
                lsbx_users.insert('end', text)


        win_uManager.mainloop()






# ----------------------------------------------- Admin Panel -----------------------------------------------

    win_admin = tkinter.Toplevel(win)
    win_admin.title('Adminstrator Panel')
    win_admin.geometry('200x200')

    lbl_add_btn = tkinter.Label(win_admin, text='Add New Products')
    lbl_add_btn.pack()
    btn_add_product = tkinter.Button(win_admin, text='Add Product', command=add_product)
    btn_add_product.pack()

    lbl_line1 = tkinter.Label(win_admin, text='')
    lbl_line1.pack()

    lbl_qnt_add = tkinter.Label(win_admin, text='Product Quantity De/Increment')
    lbl_qnt_add.pack()
    btn_inde = tkinter.Button(win_admin, text='De/Increase Quantities', command=deincrement)
    btn_inde.pack()

    lbl_line2 = tkinter.Label(win_admin, text='')
    lbl_line2.pack()

    lbl_user_mngr = tkinter.Label(win_admin, text='User Manager')
    lbl_user_mngr.pack()
    btn_user_manager = tkinter.Button(win_admin, text='User Manager', command=user_manager)
    btn_user_manager.pack()

    win_admin.mainloop()






# ----------------------------------------------- Main -----------------------------------------------

win = tkinter.Tk()
win.title("SHOP PROJECT")
win.geometry("300x300")

session = False

lbl_user = tkinter.Label(win, text="Username:")
lbl_user.pack()

txt_user = tkinter.Entry(win)
txt_user.pack()


lbl_pass = tkinter.Label(win, text="Password:")
lbl_pass.pack()

txt_pass = tkinter.Entry(win)
txt_pass.pack()

lbl_msg = tkinter.Label(win, text = "")
lbl_msg.pack()

btn_login = tkinter.Button(win, text="Login", command=login)
btn_login.pack()

btn_submit = tkinter.Button(win, text="Submit", command=submit)
btn_submit.pack()

btn_logout = tkinter.Button(win, text="Logout", command=logout, state='disabled')
btn_logout.pack()

btn_shop = tkinter.Button(win, text="Shop", command=shop, state='disabled')
btn_shop.pack()

btn_cart = tkinter.Button(win, text="My cart", command=mycart, state='disabled')
btn_cart.pack()

btn_admin = tkinter.Button(win, text='Admin Panel', state='disabled', command=admin)
btn_admin.pack()


win.mainloop()