numberLargest=int(input("Enter Largest number:"))
numbersmallest=int(input("Enter smallest number:"))

while(numbersmallest):
    numberstore=numbersmallest
    numbersmallest=numberLargest%numbersmallest
    numberLargest=numberstore
print("HCF is :",numberLargest)