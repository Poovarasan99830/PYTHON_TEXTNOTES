
# __________________________________________________________________
## 🟢 **Day 9 – Sets & Duplicate Problems**
# __________________________________________________________________

### ⏱ Learn

* **Set (unique elements)**
* Detect duplicates quickly
* Membership checking

---

### 🧠 Problems

1️⃣ **Contains duplicate**
2️⃣ **Remove duplicates**
3️⃣ **Find first duplicate**


🎯 **Pattern:** Set lookup

<!-- Find First Duplicate -->


Input:  [2, 1, 3, 5, 3, 2]
Output: 3



data=[2, 1, 3, 5, 3, 2]

seen=set()
for i in data:
    if i in seen:
        print(i)
        break
    seen.add(i)


| Step | num | seen      | Action                       |
| ---- | --- | --------- | ---------------------------- |
| 1    | 2   | {}        | add                          |
| 2    | 1   | {2}       | add                          |
| 3    | 3   | {2,1}     | add                          |
| 4    | 5   | {2,1,3}   | add                          |
| 5    | 3   | {2,1,3,5} | 🔥 already உள்ளது → RETURN 3 |


| Problem         | Use |
| --------------- | --- |
| duplicate check | set |
| unique values   | set |
| fast lookup     | set |
| seen before     | set |


We need a structure that:
   Stores only unique values
   Checks existence fast (O(1))
   👉 That’s exactly what a SET does.
   A Set = Collection of UNIQUE elements



Why fast?
   Set uses hashing (like dictionary keys)
   is very fast ⚡ (O(1))



Why use Set?
    To remove duplicates and check fast
   

Why fast checking needed?
    👉 Because checking in list is slow
   


Why list is slow?
    👉 Because list must check each element one by one


Why set is fast?
     👉 Because of hashing (direct address access)


Why hashing works?
    👉 Each element converted to hash value (index-like)
    So instead of searching:
    ➡️ It directly jumps to location