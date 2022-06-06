import  pymssql
#
# conn=pymssql.connect(
#     server="192.168.88.124",
#     user="sa",
#     password="ZMH11.",
#     database="MDEBR",
#     autocommit=True,
#     port='1433',
#     as_dict=True
# )
# cur=conn.cursor()
# if cur:
#     print(cur)
#
#
# sql="select * from XPHARMA_USER_CERT_FILES;"
#
# f=cur.execute(sql)
# print(type(f),f)
# a=cur.fetchone()
# print(a)
# b=cur.fetchall()
# print(b)
# cur.close()


def sss(*a):
    for i in a:

        print("a={}".format(i))
        print("b={}".format(i))
        print("c={}".format(i))

sss(1,2,3,4,)

a=[1,2]
a.sort()
b=[2,1]
b.sort()
print(a==b)