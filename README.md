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

Fork this repository and produce one or more example use case and and design documentation for:

1) The language or UI that the end user uses to select/configure and compose an automation job
2) Your "SDK" for adding new triggers/operations and outputs. This should include documemtation and samples.
3) A limited working example demostrating aspects of the solution

### Use case demonstration

A demonstration of the main idea of the solutions must show:

1) A business user's experience in creating and setting up an automation job. The user must be able to choose what will trigger the task, choose at least two operations to perform and choose a way to produce some sort of output from the automation.
2) A business user's experience for viewing the results of an automation job.
3) A business user's experience for modifying an automation job. The user must be able to define an intermediate processing task that uses something produced by a previous task.
4) A developer's expierence for adding a new trigger, processing task or output task.
5) The business user's experience for swapping out an existing trigger, processing task or output task with the new one added in step 4 above.

### Prereqisites

Pick your own use cases as a subject for your project.

You may use python and/or javascript and open source libraries instalable via pip or npm.
You provide your own execution environment or run on Amazon Lambda or Google Cloud Functions
All source code needed to demonstrate your example should be present in your repository along with documentation about how to setup and use it.

## Evaluation Criteria

1) Ease of composition. How easy is it for non-technical users to compose multi-sequence tasks?
2) Ease of authoring? How easy is it for developers to contribute new triggers/operation or output types?
3) How broad is the range of configuration and composition options provided?
4) How useful would this be to a real user? Your solution will be somewhat useful to a user if it allows the user to automate something that he/she currently does manually. It will be even more useful if it allows the users to do something that he/she couldn't do at all today.
 
