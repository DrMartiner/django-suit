from django.utils.unittest.case import TestCase
from suit.widgets import LinkedSelect, HTML5Input, EnclosedInput, \
    NumberInput, SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
from django.utils.translation import ugettext as _


class WidgetsTestCase(TestCase):
    def test_NumberInput(self):
        inp = NumberInput()
        self.assertEqual('number', inp.input_type)

    def test_HTML5Input(self):
        input_type = 'calendar'
        inp = HTML5Input(input_type=input_type)
        self.assertEqual(input_type, inp.input_type)

    def test_LinkedSelect(self):
        ls = LinkedSelect()
        self.assertTrue('linked-select' in ls.attrs['class'])

    def test_LinkedSelect_with_existing_attr(self):
        ls = LinkedSelect(attrs={'class': 'custom-class', 'custom': 123})
        self.assertEquals('linked-select custom-class', ls.attrs['class'])
        self.assertEquals(ls.attrs['custom'], 123)

    def render_enclosed_widget(self, enclosed_widget):
        return enclosed_widget.render('enc', 123)

    def get_enclosed_widget_html(self, values):
        return '<div class="input-prepend input-append">%s<input name="enc" ' \
               'type="text" value="123" />%s</div>' % values

    def test_EnclosedInput_as_text(self):
        inp = EnclosedInput(prepend='p', append='a')
        output = self.render_enclosed_widget(inp)
        result = ('<span class="add-on">p</span>',
                  '<span class="add-on">a</span>')
        self.assertEqual(output, self.get_enclosed_widget_html(result))

    def test_EnclosedInput_as_icon(self):
        inp = EnclosedInput(prepend='icon-fire', append='icon-leaf')
        output = self.render_enclosed_widget(inp)
        result = ('<span class="add-on"><i class="icon-fire"></i></span>',
                  '<span class="add-on"><i class="icon-leaf"></i></span>')
        self.assertEqual(output, self.get_enclosed_widget_html(result))

    def test_EnclosedInput_as_html(self):
        inp = EnclosedInput(prepend='<em>p</em>', append='<em>a</em>')
        output = self.render_enclosed_widget(inp)
        result = ('<em>p</em>', '<em>a</em>')
        self.assertEqual(output, self.get_enclosed_widget_html(result))

    def test_SuitDateWidget(self):
        sdw = SuitDateWidget()
        self.assertTrue('vDateField' in sdw.attrs['class'])

    def test_SuitDateWidget_with_existing_class_attr(self):
        sdw = SuitDateWidget(attrs={'class': 'custom-class'})
        self.assertTrue('vDateField ' in sdw.attrs['class'])
        self.assertTrue(' custom-class' in sdw.attrs['class'])
        self.assertEqual(_('Date:')[:-1], sdw.attrs['placeholder'])

    def test_SuitDateWidget_with_existing_placeholder_attr(self):
        sdw = SuitDateWidget(attrs={'class': 'custom-cls', 'placeholder': 'p'})
        self.assertTrue('vDateField ' in sdw.attrs['class'])
        self.assertTrue(' custom-cls' in sdw.attrs['class'])
        self.assertEqual('p', sdw.attrs['placeholder'])

    def get_SuitDateWidget_output(self):
        return '<div class="input-append suit-date"><input class="vDateField ' \
               'input-small " name="sdw" placeholder="Date" ' \
               'size="10" type="text" /><span class="add-on"><i ' \
               'class="icon-calendar"></i></span></div>'

    def test_SuitDateWidget_output(self):
        sdw = SuitDateWidget(attrs={'placeholder': 'Date'})
        output = sdw.render('sdw', '')
        self.assertEquals(
            self.get_SuitDateWidget_output(), output)

    def test_SuitTimeWidget(self):
        sdw = SuitTimeWidget()
        self.assertTrue('vTimeField' in sdw.attrs['class'])

    def test_SuitTimeWidget_with_existing_class_attr(self):
        sdw = SuitTimeWidget(attrs={'class': 'custom-class'})
        self.assertTrue('vTimeField ' in sdw.attrs['class'])
        self.assertTrue(' custom-class' in sdw.attrs['class'])
        self.assertEqual(_('Time:')[:-1], sdw.attrs['placeholder'])

    def test_SuitTimeWidget_with_existing_placeholder_attr(self):
        sdw = SuitTimeWidget(attrs={'class': 'custom-cls', 'placeholder': 'p'})
        self.assertTrue('vTimeField ' in sdw.attrs['class'])
        self.assertTrue(' custom-cls' in sdw.attrs['class'])
        self.assertEqual('p', sdw.attrs['placeholder'])

    def get_SuitTimeWidget_output(self):
        return '<div class="input-append suit-date suit-time"><input ' \
               'class="vTimeField input-small " name="sdw" ' \
               'placeholder="Time" size="8" type="text" /><span ' \
               'class="add-on"><i class="icon-time"></i></span></div>'

    def test_SuitTimeWidget_output(self):
        sdw = SuitTimeWidget(attrs={'placeholder': 'Time'})
        output = sdw.render('sdw', '')
        self.assertEquals(
            self.get_SuitTimeWidget_output(),
            output)

    def test_SuitSplitDateTimeWidget(self):
        ssdtw = SuitSplitDateTimeWidget()
        output = ssdtw.render('sdw', '')
        dwo = self.get_SuitDateWidget_output().replace('sdw', 'sdw_0')
        two = self.get_SuitTimeWidget_output().replace('sdw', 'sdw_1')
        self.assertEquals(output, '<div class="datetime">%s %s</div>' %
                                  (dwo, two))
