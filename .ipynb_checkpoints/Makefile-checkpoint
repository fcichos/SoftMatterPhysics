# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = -v
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

github:
	@make html
	@cp -a build/html/. ./docs
    
NOTEBOOK_DIR := ./source/notebooks
IPYNB_FILES := $(shell find ./source/notebooks/L*/ -name '*.ipynb' | grep -v '\.ipynb_checkpoints/')

pdf:
	@for file in $(IPYNB_FILES); do \
        echo "Processing $$file"; \
        jupyter nbconvert $$file --to pdf --no-input; \
    done
    
# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

