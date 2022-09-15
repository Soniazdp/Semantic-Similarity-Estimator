# Semantic Similarity
In this project, an intelligent system is built to estimate the *semantic similarity* of any given pair of words. In this way, the system can quickly find the synonym of a word, provided a group of candidates.

The semantic similarity is measured using the *semantic descriptor vector* of each word, which is represented as $desc_w = \{w_i: n_i\}$ where $n_i$ is the number of sentences in which both the word $w$ and $w_i$ have appeared. For example, in the paragraph 

> I am a sick man. I am a spiteful man. I am an unattractive man. 
>
> ​                                  -- From *Notes from the Underground* by Fyodor Dostoyevsky

$desc_{'man'} = \{'i':3, ~'am':3, ~'a': 2\, ~'sick':1, ~'spiteful':1, ~'an':1, ~'unattractive':1\}$. The semantic descriptor vector of each word can be therefore expressed in a similar way, which are vectors $u = \{u_1, u_2, ..., u_n\}$ and $v=\{v_1, v_2, ..., v_n\}$.

Thus, the semantic similarity of the words, $u$ and $v$, can be calculated as 
$$
sim(u,v) = \frac{u \cdot v}{|u||v|} = \frac{\sum_{i=1}^{n} u_i v_i}{\sqrt{(\sum_{i=1}^{n}u_i^2)(\sum_{i=1}^{n}v_i^2)}}
$$
where $u_i v_i$ is the product of the number of times that the given word appears together with the word $u_i$ and that it apears together with the word $v_i$. In other words, if a word only appears with $u$, but not $v$, the product of $u_i v_i$ will equal 0. 

After comparing with all candidates, the word with the highest similarity will be chosen as the synonym. 

## Usage

### Directory Structure

- `sw.txt`, `wp.txt` and `test.txt`: all text files that are used to retrieve the synonym of a given word.
- `synonyms.py`: contains all functions to clean up the texts and calculate the semantic similarity.

### Testing Example 

The functionality can be tested using codes similar to the following:

```
sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
print(res, "of the guesses were correct")
```



## Credit
The starter code of this project is provided by Michael Guerzhoy for the course ESC180, while the full functionality was achieved by Bonnie Luo and Sonia Zeng in the 2020 Fall.

