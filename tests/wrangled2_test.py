
from my_lambdata.assignment1 import WrangledFrame


    def test_add_state_names(self):
        wf = WrangledFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
        #self.assertEqual(list(wf.columns, ['abbrev']))
        assert list(wf.columns) == ['abbrev']

        wf.add_state_names()
        # ensure there is a "name" column
        assert (list(wf.columns) == ['abbrev', 'name'])
        # ensure the values of WF are specific classes/values
        # (string, "California")
        assert (wf["name"][0], "California")
        assert (wf["abbrev"][0], "CA")
