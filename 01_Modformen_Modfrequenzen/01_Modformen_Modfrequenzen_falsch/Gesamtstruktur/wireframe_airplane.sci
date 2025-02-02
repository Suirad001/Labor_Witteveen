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
    scatter3d(xy(:,1), xy(:,2), imMode1, "fill",  "markerFaceColor", "black")
    param3d(xy(:,1), xy(:,2), imMode1, 0, 1)
    
//Zeichnen der verformten Struktur für Mode 1 (ca. 1.5 Hz)
//=======================================================
    //Anregung am Tragflügel
    //----------------------
    imMode1Tragfl = zeros(5,1)
    imMode1Tragfl(1) = 155.24
    imMode1Tragfl(2) = 514.69
    imMode1Tragfl(3) = 849.88
    imMode1Tragfl(4) = 403.32
    imMode1Tragfl(5) = 172.65
    
    //Anregung am Rumpf
    //-----------------
    imMode1Rumpf = zeros(5,1)
    imMode1Rumpf(1) = 238.49
    imMode1Rumpf(2) = 2001.16
    imMode1Rumpf(3) = 365.84
    imMode1Rumpf(4) = 617.81
    imMode1Rumpf(5) = 38.58
    
    //Anregung an Finne
    //-----------------
    imMode1Finne = zeros(5,1)
    imMode1Finne(1) = 212.56
    imMode1Finne(2) = 123.47
    imMode1Finne(3) = 134.51
    imMode1Finne(4) = 85.57
    imMode1Finne(5) = 32.28
    
    //Aufruf des Plots
    //----------------
    scatter3d(xy(1:5,1), xy(1:5,2), imMode1Tragfl, "fill", "markerFaceColor", "red")
    param3d(xy(1:5,1), xy(1:5,2), imMode1Tragfl, 0, 1)
    scatter3d(xy(6:10,1), xy(6:10,2), imMode1Rumpf, "fill", "markerFaceColor", "green")
    param3d(xy(6:10,1), xy(6:10,2), imMode1Rumpf, 0, 1)
    scatter3d(xy(11:15,1), xy(11:15,2), imMode1Rumpf, "fill", "markerFaceColor", "cyan")
    param3d(xy(11:15,1), xy(11:15,2), imMode1Rumpf, 0, 1)
    
    title("Mode 1 des Flugzeugs bei f = 1,2 [Hz]")
    xlabel("x-Achse [cm]")
    ylabel("y-Achse [cm]")
    axes = gca()
    axes.data_bounds = [-90,90,-10,150,-1,2500]
