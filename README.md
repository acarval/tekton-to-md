# tekton-to-md
Python script to generate documentation from a tekton file


## 1- Installation

######1. Clone repository
```
clone https://github.com/acarval/tekton-to-md.git
```

######2. Install python if you don't have it

######3. Run script

```
python3 generate-documentation.py ./tekton ./documentation

```

**Param 1:** Tekton's sources folder path
**Param 2:** Folder's path where the documentation will be generated

> :warning: The script will delete the old documentation if there is any files in the documentation path prodived 


## 2- Example

```
python3 generate-documentation.py ./tekton-example ./documentation-example

```

**.tekton-example**: Tekton yaml files are retrieve from https://github.com/open-toolchain/tekton-catalog repository. 
