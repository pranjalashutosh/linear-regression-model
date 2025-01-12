from collections import defaultdict

salaries_and_tenure = [(83000, 8.7),(88000, 8.1),
                       (48000, 0.7),(76000, 6),
                       (69000, 6.5),(76000, 7.5),
                       (60000, 2.5),(83000, 10),
                       (48000, 1.9),(63000, 4.2)]

salaryBasedOnTenure = defaultdict(list)

for salary, tenure in salaries_and_tenure:
      salaryBasedOnTenure[tenure].append(salary)

#print(salaryBasedOnTenure)
      

def tenure_range(tenure):
       if tenure < 2:
            return "less than two"
       elif tenure < 5:
            return "between 2 and 5"
       else:
            return "more than five"

bucket = defaultdict(list)

for salary, tenure in salaries_and_tenure:
      bucket[tenure_range(tenure)].append(salary)


for grp in bucket:
      print(f" {grp}: {sum(bucket[grp])/len(bucket[grp])}")
      
# Read more in chapter 14 