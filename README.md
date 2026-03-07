# Algo-Abstraction-HW2
TEAM: Emma Baumgartner, 83178781 August Williams, 54466017

Instructions to compile/build the code:
- Clone the repository
- This project does not require additional installations. 

Any assumptions (input/output format, dependencies, etc.)
- Input format:
    k m
r1 r2 r3 ... rm
- Output format
 FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>
- Example Command:  
      9 5  
      1 3 2 3 1  

Written Component Solutions:
## Question 1: Empirical Comparison

Use **at least three nontrivial input files** (each containing 50 or more requests).

For each file, report the number of cache misses for each policy.

| Input File | k | m | FIFO | LRU | OPTFF |
| :---- | :---- | :---- | :---- | :---- | :---- |
| file1 | 13 | 100 | 37 | 41 | 24 |
| file2 | 9 | 100 | 69 | 67 | 38 |
| file3 | 18 | 100 | 29 | 27 | 20 |

 

Briefly comment:

* Does OPTFF have the fewest misses?  
  * Yes  
* How does FIFO compare to LRU?  
  * They are about the same

---

## Question 2: Bad Sequence for LRU or FIFO

For ( k \= 3 ), investigate whether there exists a request sequence for which OPTFF incurs **strictly fewer misses** than LRU (or FIFO).

* If such a sequence exists:  
  * Construct one.  
  * Compute and report the miss counts for both policies.  
* If you believe no such sequence exists for the policy you chose:  
  * Provide a clear justification.

ANSWER:

Note from **theorem**: FF is optimal offline eviction algorithm

* LRU is k-competitive for any sequence of requests r, LRU(r)  kFF(r) \+ k  
* Therefore, there is a sequence outside of the k-competitive bounds that has it so that OPTFF incurs fewer misses than LRU.  
* LRU makes choices based on the past, Belady’s makes choices based on the future.  
* **A,B,C**,D,A,B,C,D  
  * LRU \- 8  
  * OPTFF \- 5
