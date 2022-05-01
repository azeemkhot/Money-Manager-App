navigation_helper = """

<IconListItem>:

    IconLeftWidget:
        icon: root.icon

Screen:
    MDToolbar:
        id:toolbar
        title:'Home'
        pos_hint:{'top':1}
        left_action_items:[["menu",lambda x:nav_drawer.set_state()]]
        right_action_items:[["dots-vertical",lambda x:app.callback(x)]]
        elevation:10


    MDNavigationLayout:
        x: toolbar.height
        size_hint_y: 1.0 - toolbar.height/root.height
        ScreenManager:
            id: screen_manager
            
            HomeScreen:
                name: "home"
                on_pre_enter: toolbar.title='Home'
   
            Screen:
                name: "new"
                on_pre_enter: toolbar.title='Add Records'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDBoxLayout:
                        padding: "24dp", "8dp", 0, "2dp"
                        adaptive_size: True
                        MDLabel:
                            text:'Select Category'
                            font_style: 'Overline'
                            font_size: 15
                            bold: True
                            adaptive_size: True
                        
                    ScrollView:
                        
                        MDList:
                        
                            TwoLineIconListItem:
                                text:'Books'
                                secondary_text:'Education, Comics, Literature'
                                on_release:app.show_new_record_dialog('Books')
                                IconLeftWidget:
                                    icon:'book-open-page-variant'
                                    
                            TwoLineIconListItem:
                                text:'Clothing'
                                secondary_text:'Shirts, Pants, Shoes, Accessories'
                                on_release:app.show_new_record_dialog('Clothing')
                                IconLeftWidget:
                                    icon:'tshirt-crew'
                                    
                            TwoLineIconListItem:
                                text:'Education'
                                secondary_text:'School/College Fees, Tuition Fees, Extracurricular Activities, Supplies'
                                on_release:app.show_new_record_dialog('Education')
                                IconLeftWidget:
                                    icon:'school'
                                    
                            TwoLineIconListItem:
                                text:'Entertainment'
                                secondary_text:'Games, Movies, Concerts, Vacations, Subscriptions'
                                on_release:app.show_new_record_dialog('Entertainment')
                                IconLeftWidget:
                                    icon:'movie-open'
                                    
                            TwoLineIconListItem:
                                text:'Food'
                                secondary_text:'Restaurants, Snacks'
                                on_release:app.show_new_record_dialog('Food')
                                IconLeftWidget:
                                    icon:'food'
                                
                            TwoLineIconListItem:
                                text:'Groceries'
                                secondary_text:'Vegetables, Grains, Spices, Fruits'
                                on_release:app.show_new_record_dialog('Groceries')
                                IconLeftWidget:
                                    icon:'cart-variant'
                                
                            TwoLineIconListItem:
                                text:'Healthcare'
                                secondary_text:'Primary Care, Dental Care, Medications, Medical Devices'
                                on_release:app.show_new_record_dialog('Healthcare')
                                IconLeftWidget:
                                    icon:'hospital-box'
                                
                            TwoLineIconListItem:
                                text:'Personal'
                                secondary_text:'Gym, Salon, Cosmetics'
                                on_release:app.show_new_record_dialog('Personal')
                                IconLeftWidget:
                                    icon:'account-plus'
                                
                            TwoLineIconListItem:
                                text:'Stationery'
                                secondary_text:'Notebooks, Printouts, Writing Materials'
                                on_release:app.show_new_record_dialog('Stationery')
                                IconLeftWidget:
                                    icon:'printer'
                                
                            TwoLineIconListItem:
                                text:'Travel'
                                secondary_text:'Trains, Bus, Cabs, Car Maintenance'
                                on_release:app.show_new_record_dialog('Travel')
                                IconLeftWidget:
                                    icon:'train-car'
                                
                            TwoLineIconListItem:
                                text:'Utilities'
                                secondary_text:'Electricity, Water, Phones, Cable, Internet'
                                on_release:app.show_new_record_dialog('Utilities')
                                IconLeftWidget:
                                    icon:'tools'
                                    
                            OneLineIconListItem:
                                text:'Others'
                                on_release:app.show_new_record_dialog('Others')
                                IconLeftWidget:
                                    icon:'plus-circle'
                
            ViewScreen:
                name: "view"
                on_pre_enter: toolbar.title='View Records'

            Screen:
                name: "settings"
                on_pre_enter: toolbar.title='Settings'
                MDFloatLayout:

                    MDLabel:
                        text: "Theme"
                        font_style: 'Body1'
                        pos_hint:{'center_x': 0.55, 'center_y': 0.925}

                    MDFillRoundFlatButton:
                        text: "Open theme picker"
                        pos_hint: {'center_x': .75, 'center_y': .925}
                        size_hint: 0.45,0.075
                        on_release: app.show_theme_picker()

                    MDTextButton:
                        text:'Change Name'
                        font_style:'Button'
                        pos_hint: {'x':0.05, 'center_y': .8}
                        on_release:app.show_name_dialog()

                    MDTextButton:
                        text:'Change Email'
                        font_style:'Button'
                        pos_hint: {'x':0.05, 'center_y': .7}
                        on_release:app.show_email_dialog()
                        
                    MDTextButton:
                        text:'Delete All Records'
                        font_style:'Button'
                        pos_hint: {'x':0.05, 'center_y': .6}
                        on_release:app.delete_records()

        MDNavigationDrawer:
            id:nav_drawer
            ContentNavigationDrawer:
                id:cnd
                screen_manager: screen_manager
                nav_drawer: nav_drawer
   

<ContentNavigationDrawer>:
    nameid : nameid
    emailid : emailid
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    MDIcon:
        icon:"account-circle"
        size_hint_y: None
        height: self.texture_size[1]
        font_size: 70

    MDLabel:
        id:nameid
        text: ""
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        id:emailid
        text: ""
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        MDList:

            OneLineIconListItem:
                text: "Home"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "home"
                IconLeftWidget:
                    icon:"home"
                    
            OneLineIconListItem:
                text: "Add Records"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "new"
                IconLeftWidget:
                    icon:"plus"
                    
            OneLineIconListItem:
                text: "View Records"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "view"
                IconLeftWidget:
                    icon:"view-list"

            OneLineIconListItem:
                text: "Settings"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "settings"
                IconLeftWidget:
                    icon:"cog"

<HomeScreen>:
    ScrollView:
        ltd:ltd
        thm:thm
        mec:mec
        MDBoxLayout:
            spacing: '7dp'
            padding: '7dp'
            orientation:'vertical'
            adaptive_height: True
            size_hint_y: None
            size_hint_x: 1.0
                
            MDBoxLayout:
                ltd:ltd
                orientation:'vertical'
                adaptive_height: True
                adaptive_width: True
                size_hint_y: None
                size_hint_x: 1.0
                MDLabel:
                    text:'Last 30 Days'
                    font_style: 'Button'
                    md_bg_color: app.theme_cls.primary_light
                    halign: 'center'
                    size_hint: 1.0, None  
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                
                MDLabel:
                    id: ltd
                    text:'0'
                    font_style: 'H5'
                    md_bg_color: app.theme_cls.primary_light
                    halign: 'center'
                    size_hint: 1.0, None    
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            MDBoxLayout:
                thm:thm
                orientation:'vertical'
                adaptive_height: True
                adaptive_width: True
                size_hint_y: None
                size_hint_x: 1.0
                MDLabel:
                    text:'This Month'
                    font_style: 'Button'
                    md_bg_color: app.theme_cls.primary_color
                    halign: 'center'
                    size_hint: 1.0, None  
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    
                MDLabel:
                    id: thm
                    text:'0'
                    font_style: 'H5'
                    md_bg_color: app.theme_cls.primary_color
                    halign: 'center'
                    size_hint: 1.0, None  
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            MDBoxLayout:
                mec:mec
                orientation:'vertical'
                adaptive_height: True
                adaptive_width: True
                size_hint_y: None
                size_hint_x: 1.0    
                MDLabel:
                    text:'Most Expensive Category'
                    font_style: 'Button'
                    md_bg_color: app.theme_cls.primary_light
                    halign: 'center'
                    size_hint: 1.0, None  
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    
                MDLabel:
                    id:mec
                    text:''
                    md_bg_color: app.theme_cls.primary_light
                    font_style: 'H5'
                    halign: 'center'
                    size_hint: 1.0, None  
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                
            Image:
                id:pchimg
                source: "catamt.png"
                size_hint_x: None
                size_hint_y: None
                width: "300dp"
                height: "300dp"                            

<ViewScreen>:
    MDBoxLayout:
        selection_list:selection_list
        noreclabel:noreclabel
        orientation: 'vertical'
        MDBoxLayout:
            padding: "24dp", "8dp", 0, "2dp"
            adaptive_size: True
            
            MDLabel:
                text: "All Records"
                font_style: "Overline"
                font_size: 15
                bold: True
                adaptive_size: True
        
        MDFloatLayout:    
            selection_list:selection_list
            MDLabel:
                id: noreclabel
                text: "No Records to display"
                halign: 'center'
                font_style: "Body2"
                pos_hint: {"center_x": 0.5, "center_y": 0.55}
                #adaptive_size: True
          
            ScrollView:  
                MDSelectionList:
                    id: selection_list
                    

<ContentNameDialog>:
    name:name
    orientation:'vertical'
    size_hint_y: None
    height: "40dp"

    MDTextField:
        id:name
        hint_text:'Enter New Name'
        required: True
        helper_text_mode: "on_error"
        helper_text: "Required"


<ContentEmailDialog>:
    email:email
    orientation:'vertical'
    size_hint_y: None
    height: "40dp"

    MDTextField:
        id:email
        hint_text:'Enter New Email'
        required: True
        helper_text_mode: "on_error"
        helper_text: "Required"
        
<ContentNewRecordDialog>:
    rname:rname
    amt:amt
    dmy:dmy
    orientation:'vertical'
    size_hint_y: None
    height: "170dp"
    spacing:'10dp'
    
    MDTextField:
        id:rname
        hint_text:'Record name'
        required: True
        helper_text_mode: "on_error"
        helper_text: "Required"
        
    MDTextField:
        id:amt
        hint_text:'Amount'
        required: True
        helper_text_mode: "on_error"
        helper_text: "Required"
        
    MDTextField:
        id:dmy
        hint_text:'DD-MM-YYYY'
        required: True
        helper_text_mode: "on_error"
        helper_text: "Required"
        
"""
