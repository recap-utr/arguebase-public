# [Argdown Examples](https://github.com/christianvoigt/argdown/tree/master/examples)

Released under the MIT license by Christian Voigt.

## Convert to JSON

```shell
npx @argdown/cli json "argdown-examples/format=argdown,lang=en/*.argdown" "argdown-examples/format=argdown-json,lang=en" && prettier --write "argdown-examples/format=argdown-json,lang=en"
```
