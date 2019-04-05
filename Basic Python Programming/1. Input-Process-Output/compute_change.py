
amount = float(input("Enter an amount, for example 11.56\n"))

remaining_amount = int(amount * 100)

number_of_OneDollars = remaining_amount//100
remaining_amount = remaining_amount%100

number_of_Quarters = remaining_amount // 25
remaining_amount = remaining_amount % 25

number_of_Dimes = remaining_amount // 10
remaining_amount = remaining_amount % 10

number_of_Nickels = remaining_amount//5
remaining_amount = remaining_amount % 5

number_of_Pennies = remaining_amount

print("Your amount", amount, "consists of \n", \
        "\t", number_of_OneDollars, "dollars \n" \
        "\t", number_of_Quarters, "quarters \n" \
        "\t", number_of_Dimes, "dimes \n" \
        "\t", number_of_Nickels, "nickles \n" \
        "\t", number_of_Pennies, "pennies \n" \
      )
