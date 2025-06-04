# My List Manager - Mini app project for practice
# App features -
#   - เพิ่มรายการของลง dict (ชื่อ → หมวดหมู่)
#   - ดูรายการทั้งหมด
#   - ลบรายการ
#   - ออกจากโปรแกรม
'''
#เพิ่มรายการของ ลงdict (ชื่อ : หมวดหมู่)
def add_items(my_list):
    name = input(f"ชื่อของ: ")
    catagory = input(f"หมวดหมู่: ")
    my_list[name] = catagory
    print(f"✅ เพิ่ม '{name}' เรียบร้อยแล้ว!")

#ดูรายการ ของทั้งหมด    
def view_items(my_list):
    if not my_list:
        print("ไม่มีของในรายการเลยจ้า 🥲")
    else:
        print("🗂 รายการของคุณ:")
        for item, cat in my_list.items():
            print(f"📌 {item} ({cat})")

#ลบรายการ ของ
def delete_item(my_list):
    name = input("ชื่อของที่ต้องการลบ: ")
    if name in my_list:
        del my_list[name]
        print(f"🗑 ลบ '{name}' เรียบร้อยแล้ว")
    else:
        print("ไม่พบของชิ้นนี้ในรายการจ้า")

#ระบบการทำงาน        
def run_app():
    my_list = {}
    while True:
        print("\n📋 เมนูหลัก:")
        print("1. เพิ่มของ")
        print("2. ดูรายการทั้งหมด")
        print("3. ลบของ")
        print("4. ออก")

        choice = input("เลือกเมนู (1-4): ")
        if choice == "1":
            add_items(my_list)
        elif choice == "2":
            view_items(my_list)
        elif choice == "3":
            delete_item(my_list)
        elif choice == "4":
            print("👋 ขอบคุณที่ใช้แอป See you!")
            break
        else:
            print("❌ เลือกแค่ 1-4 เท่านั้นน้าาา")

run_app()
'''

# My movie list

#เพิ่มรายการ
def add_movie(my_movie_list):
    movie_name = input(f"โปรดระบุชื่อหนัง: ")
    movie_catagory = input(f"โปรดระบุแนวของหนัง: ")
    my_movie_list[movie_name] = movie_catagory
    print(f"\n ได้ทำการเพิ่มรายชื่อหนัง เรียบร้อยแล้ว")
    
#ดูรายการหนังของเรา
def view_movie_list(my_movie_list):
    if not my_movie_list:
        print(f"\n ไม่มีชื่อรายการหนังที่อยู่ใน list ของคุณจ้า")
    else:
        print(f"\n รายชื่อหนังของคุณ:")
        for movie_name, movie_catagory in my_movie_list.items():
            print(f'{movie_name} ({movie_catagory})')
            
#ลบรายชื่อหนังออกจากlist
def del_movie_list(my_movie_list):
    movie_name = input(f"โปรดระบุชื่อหนังที่คุณต้องการลบออกจากรายการ: ")
    if movie_name in my_movie_list:
        del my_movie_list[movie_name]
        print(f"ทำการลบหนังออกจาก list ของคุณเรียบร้อยแล้ว")
    else:
        print(f"โปรดระบุชื่อหนังของคุณให้ถูกต้องด้วยจ้า")
        
#ระบบ
def run_app():
    my_movie_list = {}
    while True:
        print(f"\n 1. เพิ่มรายชื่อหนังใน list ของคุณ")
        print(f"\n 2. ดูรายชื่อหนังใน list ของคุณ")
        print(f"\n 3. ลบรายชื่อหนังใน list ของคุณ")
        print(f"\n 4. ปิดโปรแกรม")
        
        choice = int(input(f'โปรดระบุเลข 1-4 เพื่อทำรายการ: '))
        if choice == 1:
            add_movie(my_movie_list)
        elif choice == 2:
            view_movie_list(my_movie_list)
        elif choice == 3:
            del_movie_list(my_movie_list)
        elif choice == 4:
            print(f"ขอบคุณที่ใช้โปรแกรมของเรา")
            break
        else:
            print(f"คุณทำรายการไม่ถูกต้อง กรุณาระบุหมายเลข 1 - 4 เท่านั้น")
            
run_app()
            
        


