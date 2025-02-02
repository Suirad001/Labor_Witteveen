//=============================================================================
//                           Wireframe - Airplane
//=============================================================================

//Zeichnen der Flugzeugstruktur
//=============================
    //xy-DOF-Koordinaten
    xy = [90 30;
          40 30;
          0 30;
          -40 30;
          -90 30;
          0 0;
          0 30;
          0 60;
          0 90;
          0 140;
          30 140;
          15 140;
          0 140;
          -15 140;
          -30 140]
    
    //Dummy-Imaginärteilvektor
    len = size(xy,1)
    imMode1 = zeros(len, 1)
    
    //Aufruf des Plots
    scatter3d(xy(:,1), xy(:,2), imMode1, "fill")
    
//Zeichnen der verformten Struktur für Mode 1 (ca. 1.5 Hz)
//=======================================================
    //Anregung am Tragflügel
    //----------------------
    imMode1(1) = 155.24
    imMode1(2) = 514.69
    imMode1(3) = 849.88
    imMode1(4) = 403.32
    imMode1(5) = 172.65
    
    //Anregung am Rumpf
    //-----------------
    imMode1(6) = 238.49
    imMode1(7) = 2001.16
    imMode1(8) = 365.84
    imMode1(9) = 617.81
    imMode1(10) = 38.58
    
    //Anregung an Finne
    //-----------------
    imMode1(11) = 212.56
    imMode1(12) = 123.47
    imMode1(13) = 134.51
    imMode1(14) = 85.57
    imMode1(15) = 32.28
    
    //Aufruf des Plots
    //clf;
    scatter3d(xy(:,1), xy(:,2), imMode1, "fill", "markerFaceColor", "red")
    
