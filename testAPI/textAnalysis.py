def getLocationFromText(text, java_path, sner_classifier_path, sner_jar_path):
    """
    Returns the words identified as 'LOCATION' from a text string using the Stanford NLP NER tagger of the NLTK toolkit.
    
    Parameters:
        text (str): The text string to analyse
        java_path (str): The path location of the java executable
        sner_classifier_path (str): The path location of the stanford ner classifier
        sner_jar_path (str): The path location of the .jar file of stanford ner
        
    Returns:
        location_words (list): List of words identified as location
        
    References:
        https://pythonprogramming.net/named-entity-recognition-stanford-ner-tagger/ : use this as a setup tutorial
        https://nlp.stanford.edu/software/CRF-NER.shtml#Download : This has the required downloads
        
    Notes:
        This works okay, but doesn't work well for identifying highways, roads, trainlines, etc.
            
    """
    
    from nltk.tag import StanfordNERTagger
    from nltk.tokenize import word_tokenize
    import os
    
    
    #======================================================================
    # Here are the path names used by Sanjan - local computer
    if java_path == '':
        java_path = 'C:/Program Files/Java/jre1.8.0_221/bin/java.exe'
      
    if sner_classifier_path == '':
        sner_classifier_path = 'C:/Users/Admin/Documents/stanford-ner-2018-10-16/stanford-ner-2018-10-16/classifiers/english.muc.7class.distsim.crf.ser.gz'
    
    if sner_jar_path == '':
        sner_jar_path = 'C:/Users/Admin/Documents/stanford-ner-2018-10-16/stanford-ner-2018-10-16/stanford-ner.jar'
    
    # sample text
    if text == '':
        text = 'Meet me at Hyde Park at around 7pm this evening.'
    #======================================================================
    
    os.environ['JAVAHOME'] = java_path
    
    st = StanfordNERTagger(sner_classifier_path, sner_jar_path, encoding='utf-8')
    
    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)
    
    location_words = []
    for word in classified_text:
        if word[1]=='LOCATION':
            location_words.append(word[0])
            
    return location_words
    
    