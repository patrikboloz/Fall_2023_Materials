#!usr/bin/bash

echo "Welcome to the AwesomeCalculator2.0, where you choose your action and your 2 numbers."
# Define functions for arithmetic operations
add() {
    echo "$1 + $2" | bc
}

subtract() {
    echo "$1 - $2" | bc
}

multiply() {
    echo "$1 * $2" | bc
}

divide() {
    if  (( $(echo "$2 == 0" | bc) )); 
    then
        echo "Error: Division by zero is not allowed."
    else
        echo "scale=2; $1 / $2" | bc
    fi
}

# Perform the selected operation
select choice in Addition Substraction Multiplication Division Quit
do
    case $choice in
        Addition)
            read -p "Enter the first number: " num1
            read -p "Enter the second number: " num2
            result=$(add "$num1" "$num2")
            echo "Result: $result"
            ;;
        Substraction)
            read -p "Enter the first number: " num1
            read -p "Enter the second number: " num2
            result=$(subtract "$num1" "$num2")
            echo "Result: $result"
            ;;
        Multiplication)
            read -p "Enter the first number: " num1
            read -p "Enter the second number: " num2
            result=$(multiply "$num1" "$num2")
            echo "Result: $result"
            ;;
        Division)
            read -p "Enter the first number: " num1
            read -p "Enter the second number: " num2
            result=$(divide "$num1" "$num2")
            echo "Result: $result"
            ;;
        Quit)
            echo "Quiting the calculator. Have a great day!"
            exit
            ;;
        *)
            echo "Invalid choice. Try again."
            ;;
    esac
done


