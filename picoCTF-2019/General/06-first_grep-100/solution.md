# Problem
We put together a bunch of resources to help you out on our website! If you go over there, you might even find a flag! [https://picoctf.com/resources](https://picoctf.com/resources)

## Hints:

## Solution:

Let's download the file:
```bash
wget https://picoctf.com/resources
```

Using a simple ```grep```:
```bash
cat resources | grep picoCTF

  <li><code class="highlighter-rouge">picoCTF{r3source_pag3_f1ag}</code> (2019 competition)</li>
  <li><code class="highlighter-rouge">picoCTF{xiexie_ni_lai_zheli}</code> (2018 competition)</li>
```

Flag: picoCTF{r3source_pag3_f1ag}
