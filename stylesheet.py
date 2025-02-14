class StyleSheet:
    MAIN_STYLE = """
        QWidget {
            background: qlineargradient(
                spread:pad,
                x1:0, y1:0,
                x2:1, y2:1,
                stop:0 rgba(20, 30, 48, 255),
                stop:1 rgba(36, 59, 85, 255)
            );
            border-radius: 0px;
            color: white;
        }
        
        QLabel {
            color: white;
            font-family: 'sans-serif';
            background: transparent;
        }
    """