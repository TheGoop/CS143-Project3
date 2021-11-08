#!/usr/bin/env bash
ZIP_FILE=project3.zip
REQUIRED_FILES="convert.sh load.sql q1.sql q2.sql q3.sql q4.sql q5.sql laureate.php"

CUR_DIR=$(pwd -P)
SRC_DIR=${CUR_DIR}

#error function
function error_exit()
{
   echo -e "ERROR: $1" 1>&2
   rm -rf ${TMP_DIR}
   exit 1
}

# make sure running in container
if [ `whoami` != "cs143" ]; then
    error_exit "You need to run this script within the container"
fi

# if the source directory is passed as parameter, use it
if [ $# -eq 1 ]; then
    SRC_DIR=$1
fi

# remove the zip file if it already exists
if [ -f ${CUR_DIR}/${ZIP_FILE} ]; then
    rm -f ${CUR_DIR}/${ZIP_FILE}
fi

# change to the directory with the submission files
cd ${SRC_DIR}

# check the existence of the required files
for FILE in ${REQUIRED_FILES}
do
    if [ ! -f ${FILE} ]; then
        echo "ERROR: Cannot find ${FILE} in ${DIR}" 1>&2
        exit 1
    fi
done


# create the zip file
zip -r ${CUR_DIR}/${ZIP_FILE} . -x p3_package p3_test \\*.json \\*.del .DS_Store Thumbs.db '.git/*' '*/.DS_Store' '*/Thumbs.db' @
if [ $? -ne 0 ]; then
    error_exit "Create ${CUR_DIR}/${ZIP_FILE} failed, check for error messages in console."
fi
echo "[SUCCESS] Created '${CUR_DIR}/${ZIP_FILE}'"
exit 0
