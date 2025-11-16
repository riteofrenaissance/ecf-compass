📖 دليل استخدام ECF Compass

🚀 البداية السريعة

المتطلبات الأساسية

· Python 3.8 أو أحدث
· Git
· pip (مدير حزم Python)

التثبيت

```bash
# استنساخ المستودع
git clone https://github.com/riteofrenaissance/ecf-compass.git
cd ecf-compass

# تثبيت الاعتماديات
pip install -r requirements.txt
```

التشغيل الأول

```bash
# تشغيل الواجهة التفاعلية
python ecf_compass/main.py

# أو تشغيل الخادم المحلي
python -m http.server 8000
```

🎯 الاستخدام الأساسي

1. تهيئة البيئة

```python
from ecf_compass.core import CompassEngine
from ecf_compass.ethics import KantianFramework

# إنشاء محرك البوصلة
compass = CompassEngine()
```

2. تحليل السيناريوهات الأخلاقية

```python
# تعريف سيناريو لتحليله
scenario = {
    "description": "اتخاذ قرار في حالة تضارب المصالح",
    "actors": ["النظام الذكي", "المستخدم", "المجتمع"],
    "constraints": ["الشفافية", "العدالة", "الخصوصية"]
}

# تحليل السيناريو
analysis = compass.analyze_scenario(scenario)
print(analysis.ethical_score)
```

3. التوجيه الأخلاقي

```python
# الحصول على توصيات أخلاقية
recommendations = compass.get_recommendations(
    context=scenario,
    framework=KantianFramework()
)

for rec in recommendations:
    print(f"✅ {rec.action}: {rec.justification}")
```

⚙️ الإعداد المتقدم

التكوين المخصص

```yaml
# config.yaml
ethical_frameworks:
  - kantian
  - utilitarian
  - virtue_ethics

output_formats:
  - json
  - html
  - pdf

language: ar
```

التكامل مع الأنظمة الأخرى

```python
# التكامل مع ECF Framework
from ecf_core import EvolutionaryFramework

ecf = EvolutionaryFramework()
compass.integrate_with(ecf)
```

🔧 استكشاف الأخطاء وإصلاحها

المشاكل الشائعة

· خطأ في الاعتماديات: pip install --upgrade -r requirements.txt
· مشاكل في الذاكرة: تقليل حجم البيانات المدخلة
· أخطاء في التحليل: التحقق من صيغة البيانات المدخلة

السجلات والتقييم

```bash
# عرض سجلات التشغيل
tail -f logs/compass.log

# تقييم أداء النظام
python -m ecf_compass.benchmark
```

📞 الدعم

· التوثيق الكامل: راجع الوثائق الرسمية
· الإبلاغ عن مشاكل: GitHub Issues
· المجتمع: منتدى النقاش