**تقرير حول تجربة التعامل مع البيانات الكبيرة**

### **1. مقدمة**
تعتبر معالجة البيانات الكبيرة تحديًا في علم البيانات، خاصة عند التعامل مع ملفات ضخمة لا يمكن تحميلها في الذاكرة دفعة واحدة. في هذه التجربة، تم اختبار ثلاث طرق مختلفة لمعالجة بيانات رحلات التاكسي في نيويورك:
1. **Chunking** (تجزئة البيانات إلى أجزاء صغيرة)
2. **Dask** (مكتبة لمعالجة البيانات الكبيرة)
3. **Compression** (ضغط البيانات لتقليل حجم الملف)

### **2. منهجية العمل**
تم استخدام لغة **Python** ومكتبات مثل **Pandas, Dask** لمعالجة البيانات. تم تنفيذ العمليات التالية:
- **قراءة البيانات من ملفات CSV**.
- **دمج البيانات في ملف واحد**.
- **قياس الأداء من حيث الزمن المستغرق وحجم البيانات**.

### **3. النتائج**

| **الطريقة**   | **زمن المعالجة (ثانية)** | **متوسط مسافة الرحلة (ميل)** | **حجم الملف (MB)** |
|----------------|---------------------------|--------------------------------|---------------------|
| **Chunking**   | **12.41**                 | **8.383**                      | **635.73 MB**       |
| **Dask**       | **7.28**                  | **8.457**                      | **635.73 MB**       |
| **Compression**| **26.12**                 | **N/A**                        | **74.35 MB**        |

### **4. تحليل النتائج**
- **Chunking:** استغرقت المعالجة **12.41 ثانية** بحجم ملف **635.73 MB**. التقنية مفيدة لتقليل استهلاك الذاكرة لكنها لا تقلل من حجم الملف النهائي.
- **Dask:** كانت **الأسرع** بزمن **7.28 ثانية** مع نفس حجم الملف، مما يجعلها خيارًا ممتازًا للبيانات الكبيرة.
- **Compression:** استغرقت **26.12 ثانية** ولكنها **قللت حجم الملف بنسبة 88% إلى 74.35 MB**، مما يجعلها خيارًا مثاليًا للتخزين.

### **5. التوصيات**
- **إذا كانت الأولوية للأداء:** يوصى باستخدام **Dask** لأنه أسرع في المعالجة.
- **إذا كانت الأولوية لتوفير المساحة:** يوصى باستخدام **Compression** رغم أنه أبطأ نسبيًا.
- **إذا كان هناك قيود على الذاكرة:** يمكن استخدام **Chunking** مع معالجة تدريجية للبيانات.

### **6. الخاتمة**
توضح هذه التجربة أن اختيار الطريقة المناسبة يعتمد على **الهدف الأساسي** سواءً كان **الأداء، التخزين، أو استهلاك الذاكرة**. يمكن الجمع بين أكثر من طريقة للحصول على توازن مثالي بين السرعة والحجم.

---
**إعداد:** [اسم المستخدم]
**التاريخ:** 08 فبراير 2025

