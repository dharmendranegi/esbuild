# Serverless EsBuild - Example Project

## Purpose

Reduce the size of your lambda package sizes.

## Steps

### Install

```bash
npm i --save-dev serverless-esbuild esbuild

```

### Update serverless.yml file in plugins section

```yaml
provider:
    name: aws
    ...
plugins:
    - serverless-esbuild
```

### Review .zip file, it should be much smaller

### Additional Optimization, add package: individually: true

```yaml
provider:
    name: aws
    ...
package:
    individually: true
plugins:
    - serverless-esbuild
```

### Including extra files

If you want to include extra files in your package than see this [Link](https://www.serverless.com/framework/docs/providers/aws/guide/packaging#patterns).
