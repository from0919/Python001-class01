1. SELECT * FROM data;
import pandas as pd
import numpy as np
excel1 = pd.read_excel(r'xxxx.xlsx')
excel1

2. SELECT * FROM data LIMIT 10;
import pandas as pd
import numpy as np
excel1 = pd.read_excel(r'xxxx.xlsx')
excel1.head(3)

3. SELECT id FROM data;  //id 是 data 表的特定一列
import pandas as pd
import numpy as np
excel1 = pd.read_excel(r'xxxx.xlsx')
excel1[['id']]

4. SELECT COUNT(id) FROM data;
import pandas as pd
import numpy as np
excel1 = pd.read_excel(r'xxxx.xlsx')
 excel1['id'].sum()


5. SELECT * FROM data WHERE id<1000 AND age>30;
import pandas as pd
import numpy as np
excel1 = pd.read_excel(r'xxxx.xlsx')
excel1[(excel1['id']<1000) &(excel1['age']>30)]


6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
import pandas as pd
import numpy as np
excel1 = pd.read_excel(r'xxxx.xlsx')
excel1.groupby('id').aggregate( { 'order_id':'sum' })

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
import pandas as pd
import numpy as np
excel1 = pd.read_excel(r'xxxx.xlsx')
excel2 = pd.read_excel(r'yyyy.xlsx')
pd.merge(excel1 , excel2 , on= 'id', how='inner')

8. SELECT * FROM table1 UNION SELECT * FROM table2;
import pandas as pd
import numpy as np
excel1 = pd.read_excel(r'xxxx.xlsx')
excel2 = pd.read_excel(r'yyyy.xlsx')
pd.concat([table1 , table2])

9. DELETE FROM table1 WHERE id=10;
import pandas as pd
import numpy as np
excel1 = pd.read_excel(r'xxxx.xlsx')
excel1.drop(excel1[excel1['id']==10].index)

10. ALTER TABLE table1 DROP COLUMN column_name;
import pandas as pd
import numpy as np
excel1 = pd.read_excel(r'xxxx.xlsx')
excel1.drop('column_name',axis=1)
