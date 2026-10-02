## Concepts

- @ray.remote : mark python code for parallel execution
- task        : stateless function call (solves slow code)
- actor       : stateful object (solves updating shared var)
- .remote()   : execute task or actor
- Objectref   : promise
- .get()      : get result of tasks
- .put()      : store large object in shared mem

- Ray cluster = ray head node + worker nodes

## To run

Assuming the venv is named env and set up with the required packages `requiremnts.txt`

```bash
kubectl apply -f deploy/raycluster-sandbox.yaml
kubectl port-forward -n ray-tutorial svc/ray-tutorial-sandbox-head-svc 8265:8265
```
```bash
./env/bin/ray job submit --address http://127.0.0.1:8265 --working-dir getting-started --no-wait -- python actor_script.py
```
