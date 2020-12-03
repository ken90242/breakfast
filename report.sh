#!/bin/sh

SQL_EXEC_ERROR=2
AWK_PARSE_ERROR=3

function exit_with_error()
{
    # $1: error code
    # $2: error statement
    echo "Failed to exectue '$2'"
    return $1
}


SQL_STATEMENT="SELECT p.shop_id, SUM(o.qty * p.price), SUM(o.qty), COUNT(1) FROM product_product as p LEFT OUTER JOIN order_order as o WHERE p.id = o.product_id GROUP BY p.shop_id;"

# Execute SQL query
RESULT=`/Users/ken/Downloads/sqlite-tools-osx-x86-3330000/sqlite3 ./db.sqlite3 "${SQL_STATEMENT}"` || exit_with_error "./sqlite3 ~/breakfast/db.sqlite3 ${SQL_STATEMENT}" "${SQL_EXEC_ERROR}"

# Generate Report
echo "${RESULT}" | awk '
    BEGIN {
        FS = "|"
        print "shop_id,total_sales,sales_volume,order_amount "
    }
    {
        print $1","$2","$3","$4
    }
    ' > report.csv || exit_with_error "awk error" "${AWK_PARSE_ERROR}"
