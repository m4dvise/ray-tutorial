## Concepts

- @ray.remote : mark python code for parallel execution
- task        : stateless function call (solves slow code)
- actor       : stateful object (solves updating shared var)
- .remote()   : execute task or actor
- Objectref   : promise
- .get()      : get result of tasks
- .put()      : store large object in shared mem