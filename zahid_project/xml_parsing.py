import xml.etree.ElementTree as ET
mytree=ET.parse('/home/autocanvas/Desktop/streetl.xodr')
myroot=mytree.getroot()
for road in myroot:
    # print(road)
    for planView in road:
        # print(planView)
        for geometry in planView:
            # print(geometry)
            for geometry_type in geometry:
                # print(geometry_type)
                for length_g in geometry_type:
                    print(length_g)
mytree.write("/home/autocanvas/Desktop/Zahid_AC_/python_zahid/py/zahid_project/venv/data/xml_output/test_1.xodr",xml_declaration=True,encoding="utf-8")


















