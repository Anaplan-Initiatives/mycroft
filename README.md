# Project Mycroft

## Goals

This project explores the possibility for allowing business users without any programming experience to compose and run their own automation tasks. 

### Hello World

A software developer can describe a "hello world" problem using a syntax like: 

```
console.log('Hello world')
```
But a business user would more likely to express their need for social interaction with a machine with something along the lines of:

```
say "hello"
```

### Not a chat bot

Chat bots are getting better at requests involving single tasks. This project concerns itself with composing multi-stage tasks like:

```
say "good morning" to me every time I wake up and play some music for me
```

This automation job has multiple elememts to it:

- a trigger
- a sequence of operations
- one or more outputs

Each of them requires some sort of configuration so that the system understands what it means in the user's context

- how does the system know when to do this?
- do they want a good morning push notification or to be greeted in some other way?
- where is this music coming from?
- what criteria should be usef for choosing music, e.g. playlist / radio station / recommendation

The main objective of this project is to explore how business users can choose from, configure and chain together known triggers, operations and outputs in an inuitive way. The examples above use natural langauage to describe the job. It is not neccessary to describe jobs in this way. You can use UI or other even a command line.

### Broader Ecosystem

So far we have only considered the end consumer of the automation service. There is work required by others to setup available triggers, operations and output types and to describe their configuration requirements. The project also explores the how the ecosystem will be enabled, e.g. as a provider or a music service, how could you allow the end consumer to use your music service to play music.

## Project and Deliverables

Fork this repository and produce one or more example use case and and design documentation for
1) The language or UI that the end user uses to select/configure and compose an automation job
2) Your "SDK" for adding new triggers/operations and outputs. This should include documemtation and samples.
3) A limited working example demostrating aspects of the solution

Pick your own example/examples to demonstrate.

You may use any open source programming lanuguage and open source libraries
You provide your own execution environment or run on Amazon Lambda or Google Cloud Functions
All source code needed to demonstrate your example should be present in your repository


## Evaluation Criteria

1) Ease of composition. How easy is it for non-technical users to compose multi-sequence tasks?
2) Ease of authoring? How easy is it for developers to contribute new triggers/operation or output types?
3) How broad is the range of configuration and composition options provided?
 
