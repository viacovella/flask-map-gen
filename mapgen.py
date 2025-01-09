import folium
import pandas as pd
from io import StringIO


def mapgen(form):
    
    # Data Loading
    
    if (form['reqtype'] == '1'):
        print("You pasted the data into the form")

        dfnames=pd.read_csv(StringIO(form['namelist']),sep=",",lineterminator=" ")
        dfcoord=pd.read_csv(StringIO(form['instlist']),sep=",",lineterminator=" ")

        print(dfcoord)
        print(dfnames)
            
          
    # basic color list taken from https://python-visualization.github.io/folium/latest/reference.html
    thecolors=['red', 'blue', 'green', 'purple', 'orange', 'darkred',
               'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
               'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
    
    def htmlpopup(df:pd.DataFrame) -> str:
        '''Transform institution name into a title and names and surnames within a dataframe into a html item list'''
        strstart="f\"\"\"<h1>" +str(pd.unique(df['istituzione'])[0])+ "</h1> "
        strbody=str(["<ul>" + str(c['nome']) + " " + str(c['cognome']) + " </ul>" for i,c in nomiCorr.iterrows()])
        strend=" \"\"\" "
        return (strstart+strbody[2:-2]+strend)
    

    # Set the map up and center it on roughly the center of Italy
    theMap = folium.Map(location = [43,12], zoom_start = 6, tiles = "CartoDB positron")

    # Populate the map with all the institutions categories
    n=0
    for t in pd.unique(dfcoord['tipologia']):
        print("tipologia: "+ t)
        currdf = pd.merge(dfnames,dfcoord[dfcoord['tipologia']==t],on='istituzione', how='inner')
        currFg = folium.FeatureGroup(name=t,show=True).add_to(theMap)
        
        for i in pd.unique(currdf['istituzione']):
            print(i)
            # Slice a DataFrame including just the current institution members
            nomiCorr=currdf[currdf['istituzione']==i]
            folium.Marker(location=[nomiCorr['long'].values[0],nomiCorr['lat'].values[0]],
                          popup=htmlpopup(nomiCorr),tooltip=i,
                          icon=folium.Icon(color=thecolors[n])).add_to(currFg)
        n=n+1
    # Create the map
    folium.LayerControl().add_to(theMap)

    return (theMap)