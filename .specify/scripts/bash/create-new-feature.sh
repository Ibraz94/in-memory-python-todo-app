#!/bin/bash

# Parse arguments
NUMBER=$1
SHORTNAME=$2
DESCRIPTION="$3"

# Create the feature branch and spec directory structure
BRANCH_NAME="${NUMBER}-${SHORTNAME}"
SPEC_DIR="specs/${BRANCH_NAME}"
SPEC_FILE="${SPEC_DIR}/spec.md"

# Create directories
mkdir -p "${SPEC_DIR}"
mkdir -p "${SPEC_DIR}/checklists"

# Create the spec file with basic content
cat > "${SPEC_FILE}" << EOF
# Specification: ${SHORTNAME}

## Feature Description
${DESCRIPTION}

EOF

# Output JSON with branch name and spec file path
cat << EOF
{
    "BRANCH_NAME": "${BRANCH_NAME}",
    "SPEC_FILE": "${SPEC_FILE}",
    "SPEC_DIR": "${SPEC_DIR}"
}
EOF