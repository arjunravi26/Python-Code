student = {
    'names': ["Alice", "Bob", "Carol", "Dave", "Eve"],
    'scores': [90, 85, 95, 80, 92]
}
import pandas as pd

new_data = pd.DataFrame(student)
print(new_data)
new_data.to_csv('student.csv')
