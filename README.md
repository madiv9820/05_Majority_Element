# [Majority Element](https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150)

#### ***Topic:- Array, Hash Table, Divide and Conquer, Sorting, Counting***

### Problem Understanding:

You’re given an array `nums` of size $\textbf{n}$, and you need to return the **majority element** in the array. The **majority element** is the element that appears more than $\frac{\textbf{n}}{\textbf{2}}$ times.

In simpler terms:
- If there’s an element that appears more than half of the time in the array, that’s the majority element.

For example:

In the array $\textbf{[3, 2, 3]}$, the element $\textbf{3}$ appears twice, which is more than half ($[\frac{\textbf{3}}{\textbf{2}}] = 1$), so $\textbf{3}$ is the majority element.

In the array $\textbf{[2, 2, 1, 1, 1, 2, 2]}$, the element $\textbf{2}$ appears **four times**, which is more than half ($[\frac{\textbf{7}}{\textbf{2}}] = \textbf{3}$), so $\textbf{2}$ is the majority element.

### Key Points:
1. **The majority element is guaranteed to exist.**
    - The problem guarantees that **there will always be** an element that appears more than half the time. So, there is no need to handle cases where no majority element exists.

2. **Linear Time:**
    - You need to solve this problem in $\textbf{O(n)}$ time, meaning you need to check each element in the array only once. That’s the minimum time required because you have to check every element to determine the majority.

3. **$\textbf{{O(1)}}$ Space:**
    - You should solve the problem using **constant space**. That means you cannot use extra space like arrays, hashmaps, or counters to store information. You can only use a fixed number of variables.