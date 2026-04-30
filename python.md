

Differences between List and Tuple : 

List is square brackets and Tuple is round brackets in syntax

Benefits of List :

1. Append ( adding value)
2. Remove ( Removes the value)
3. Pop (removes the last item of the list)
4. Indexing ( tells the position of the value in the list/array)
4. Reverse list ( tells the value from the last / [::-1])
5. Sorting ( sorts by ascending or descending )
6. prints in output 2 dimensional array
7. Gives the length (len)
8. Ranging can be  done ( ex: (1,3) which means it starts from zero)
9. Slicing can be done ( ex: 2,4)( which means it starts from 2 and ends with 3)
10.Replace can be done (ex: food[2] from an existing food item value replaces new one )
11.Inserts can be done (ex: food.insert(2, "Kheer")this will insert in the index of second position)
12.empty the list or clear (ex: food.clear() it will clear all the values in the list)
13.Sorting in descending order (ex : number.sort(reverse=True))
14.It allows deplicates!




Benefits of Tuple :

Only two benefits :

1. It gives the count
2. It gives the index 

These cannot be changed after creation or modified but allows duplicate values

Feature         |  List       |  Tuple   |  Set        |  Dictionary           
----------------+-------------+----------+-------------+-----------------------
Syntax          |  []         |  ()      |  {}orset()  |  {}with key:value     
Ordered         |  Yes        |  Yes     |  No         |  Yes (3.7+)           
Mutable         |  Yes        |  No      |  Yes        |  Yes                  
Duplicates      |  Yes        |  Yes     |  No         |  Keys: No, Values: Yes
Indexing        |  Yes ``     |  Yes ``  |  No         |  By key['key']        
Add element     |  .append()  |  N/A     |  .add()     |  dict['key'] = val    
Remove element  |  .remove()  |  N/A     |  .remove()  |  del dict['key']      

set() => empty set

set([1][2])

to create set => {}