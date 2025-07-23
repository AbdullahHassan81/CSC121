
def main():
    names = {'Tom': '910-555-5555', 'Nancy': '910-555-6666'}
    with open('contacts.txt', 'w') as contacts:
        # .write() when wanting to write 1 line at a time

        contacts.write(f'{"Name":<10}{"Phone#"}\n') #can only write string only takes 1 arguement

        for k,v in names.items():
            contacts.write(f'{k:<10}{v}\n')
if __name__ == "__main__":
    main()
