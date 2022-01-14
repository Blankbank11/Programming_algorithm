student = {100: {'Id': '100', 'Name': 'Aiy Obie', 'Age': '30', 'Sex': 'Male', 'Math': '100', 'Physic': '99', 'Programming': '100', 'Network': '100'},
          101: {'Id': '101', 'Name': 'Aiy Bank', 'Age': '2000', 'Sex': 'Female', 'Math': '0', 'Physic': '0', 'Programming': '1', 'Network': '1'},
          102: {'Id': '102', 'Name': 'John', 'Age': '24', 'Sex': 'Female', 'Math': '10', 'Physic': '30', 'Programming': '90', 'Network': '80'},
          103: {'Id': '103', 'Name': 'Jame', 'Age': '23', 'Sex': 'Female', 'Math': '60', 'Physic': '89', 'Programming': '10', 'Network': '100'},
          104: {'Id': '104', 'Name': 'Jo', 'Age': '21', 'Sex': 'Female', 'Math': '78', 'Physic': '79', 'Programming': '70', 'Network': '100'},
          105: {'Id': '105', 'Name': 'Jay', 'Age': '20', 'Sex': 'Female', 'Math': '90', 'Physic': '39', 'Programming': '80', 'Network': '100'}
          }

n = int(input("Enter ID: "))
for j in student[n]:
    print(j, " : ", student[n][j])
