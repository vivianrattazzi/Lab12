from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():


    @staticmethod
    def getAllNodes(nazione):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        results = []
        query = '''select * from go_retailers gr where Country = %s'''
        cursor.execute(query, (nazione,))
        for row in cursor:
            results.append(Retailer(**row))

        cursor.close()
        cnx.close()
        return results


    @staticmethod
    def getAllEdges(anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        results = []
        query = ''' select tab.r1, tab.r2, count(*) as prodComuni
                from(
                select gds1.Retailer_code as r1, gds2.Retailer_code as r2,  gds1.Product_number
                from go_daily_sales gds1, go_daily_sales gds2
                where gds1.Retailer_code < gds2.Retailer_code and gds1.Product_number = gds2.Product_number
                and year (gds1.`Date`) = year (gds2.`Date`) and Year(gds1.`Date`) = %s
                group by r1, r2, gds1.Product_number) as tab
                group by tab.r1, tab.r2'''
        cursor.execute(query, (anno,))
        for row in cursor:
            results.append((row['r1'], row['r2'], row['prodComuni']))

        cursor.close()
        cnx.close()
        return results



    @staticmethod
    def getNazioni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        results = []
        query = '''select distinct Country  
                from go_retailers
                '''
        cursor.execute(query)
        for row in cursor:
            results.append(row["Country"])

        cursor.close()
        cnx.close()
        return results

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        results = []
        query = '''select distinct YEAR(Date) as anno
                    from go_daily_sales gds '''
        cursor.execute(query)
        for row in cursor:
            results.append(row["anno"])

        cursor.close()
        cnx.close()
        return results




