"""ຖ້າ 80-100 ໄດ້ເກດ A
ຖ້າ 70-79 ໄດ້ເກດ B
ຖ້າ 60-69 ໄດ້ເກດ C
ຖ້າ50-59 ໄດ້ເກດ D
ຖ້າຕ່ຳກວ່າ 50 ໄດ້ເກດ F """

score = int(input("Enter your score(1-100): "))

if 80 <= score <= 100:
    print("Your grade is A")
elif 70 <= score <= 79:
    print("Your grade is B")
elif 60 <= score <= 69:
    print("Your grade is C")
elif 50 <= score <= 59:
    print("Your grade is D")
else:
    print("Congratulation!")

