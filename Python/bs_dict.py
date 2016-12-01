
html = """<table>
          <tr>
            <th width="100">menu1</th>
            <td>
              <ul class="classno1" style="margin-bottom:10;">
                    <li>Some data1</li>
                    <li>Foo1<a href="/link/to/bar1">Bar1</a></li>
              </ul>
            </td>
          </tr>
          <tr>
            <th width="100">menu2</th>
            <td>
              <ul class="classno1" style="margin-bottom:10;">
                    <li>Some data2</li>
                    <li>Foo2<a href="/link/to/bar2">Bar2</a></li>
                    <li>Foo3<a href="/link/to/bar3">Bar3</a></li>
                    <li>Some data3</li>
              </ul>
            </td>
          </tr>
</table>"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

table = soup.findAll('table')[0]

results = {}

th = table.findChildren('th')#,text=['menu1','menu2'])

for x in th:
    #print x
    results_li = []
    li = x.nextSibling.nextSibling.findChildren('li')
    for y in li:
        #print y.next
        results_li.append(y.next)
    results[x.next] = results_li

print results