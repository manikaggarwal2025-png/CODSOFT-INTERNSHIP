contacts = []

def add(): contacts.append({'name': input("Name: "), 'phone': input("Phone: "), 'email': input("Email: "), 'addr': input("Address: ")})
def view(): [print(f"{c['name']} | {c['phone']}") for c in contacts]
def search():
    q = input("Search name/phone: ").lower()
    for c in contacts:
        if q in c['name'].lower() or q in c['phone']:
            print(c); return
    print("Not found")
def update():
    n = input("Name to update: ").lower()
    for c in contacts:
        if c['name'].lower() == n:
            c['phone'] = input("New Phone: ") or c['phone']
            c['email'] = input("New Email: ") or c['email']
            c['addr'] = input("New Address: ") or c['addr']
            print("Updated"); return
    print("Not found")
def delete():
    n = input("Name to delete: ").lower()
    for c in contacts:
        if c['name'].lower() == n:
            contacts.remove(c); print("Deleted"); return
    print("Not found")

while True:
    print("\n1:Add 2:View 3:Search 4:Update 5:Delete 6:Exit")
    ch = input("Choose: ")
    if ch == '1': add()
    elif ch == '2': view()
    elif ch == '3': search()
    elif ch == '4': update()
    elif ch == '5': delete()
    elif ch == '6': break
    else: print("Invalid")
