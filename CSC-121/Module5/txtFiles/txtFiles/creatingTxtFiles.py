def main():
    names = {'Tom': '910-555-5555', 'Nancy': '910-555-6666'}

    with open('contacts.txt', 'w') as contacts:

        print(f'{"Name":<10}{"Phone#"}', file=contacts)
        print('----------------------', file=contacts)

        for k,v in names.items():

            print(f'{k:<10}{v}', file=contacts)





if __name__ == "__main__":
    main()