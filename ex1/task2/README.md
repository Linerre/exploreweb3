## What
This is the Python script for Exercise 1, task 2 of the take-home assignment required by a job interview.

## How
To try out this script, you will first need to do either of the following:

1. install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. create a virtual env using the Python installed on your local machine

I recommend uv and this doc focuses on using it. Once having it installed, you can

``` console
$ uv add web3
```
to install the required dependencies. In this case, the [web3.py](https://web3py.readthedocs.io/en/stable/index.html)

Then, simply run the below command to execute the script:

``` console
$ uv run <script-name>.py
```
where `<script-name>` can be one of the following:
1. `next_block`, to find out the next block mined by minner `0xEA674fdDe714fd979de3EdF0F56AA9716B898ec8`
2. `find_info`, to get the required info based on the block found in 1
