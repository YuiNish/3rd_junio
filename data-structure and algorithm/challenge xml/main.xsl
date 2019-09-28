<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<!--xsl:output method="html" indent="yes"
 doctype-public="-//W3C//DTD HTML 4.01//EN"
 doctype-system="http://www.w3.org/TR/html4/strict.dtd"/-->
<xsl:output method="html" indent="yes"/>
    <xsl:import-schema  schema-location="main.xsd"/>

    <xsl:template match="/">
        <xsl:apply-templates/>
    </xsl:template>

    <xsl:template match="drinklist">
        <xsl:apply-templates match="drink"/>
    </xsl:template>

    <xsl:template match="drink">
        <xsl:apply-templates match="product"/>
    </xsl:template>

    <xsl:template match="product">
        <html>
            <head>
                <title>飲み物</title>
            </head>
        <body>
            <table border="1">
            <tr>
            <th>商品名</th>
            <th>会社</th>
            <th>カロリー</th>
            <th>炭水化物</th>
            <th>食塩相当量</th>
            </tr>
            <tr>
            <td>
              <xsl:value-of select="product"/>
            </td>
            <td>
             <xsl:value-of select="company"/>
            </td>
            <td>
             <xsl:value-of select="calorie"/>kcal/100ml
            </td>
            <td>
             <xsl:value-of select="carbohydorate"/>g
            </td>
            <td>
             <xsl:value-of select="sodium"/>g 
            </td>  
            </tr>
            </table>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>