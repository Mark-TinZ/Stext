/********************************************************************************
** Form generated from reading UI file 'Stext_Image_editor.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef STEXT_IMAGE_EDITOR_H
#define STEXT_IMAGE_EDITOR_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionOpen;
    QAction *actionSave;
    QAction *actionClose;
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_3;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout;
    QPushButton *Apply;
    QCheckBox *Bin_color;
    QSpacerItem *verticalSpacer;
    QHBoxLayout *horizontalLayout_2;
    QVBoxLayout *verticalLayout_4;
    QLabel *label_2;
    QSlider *Bin_color_slider;
    QLabel *Bin_color_text;
    QVBoxLayout *verticalLayout_5;
    QLabel *label_3;
    QSlider *Scale_slider;
    QLabel *Scale_text;
    QFrame *line;
    QSpacerItem *horizontalSpacer;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QVBoxLayout *verticalLayout_2;
    QLabel *label;
    QMenuBar *menubar;
    QMenu *menuFile;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(660, 630);
        MainWindow->setMinimumSize(QSize(660, 630));
        actionOpen = new QAction(MainWindow);
        actionOpen->setObjectName(QString::fromUtf8("actionOpen"));
        actionSave = new QAction(MainWindow);
        actionSave->setObjectName(QString::fromUtf8("actionSave"));
        actionClose = new QAction(MainWindow);
        actionClose->setObjectName(QString::fromUtf8("actionClose"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout_3 = new QVBoxLayout(centralwidget);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        Apply = new QPushButton(centralwidget);
        Apply->setObjectName(QString::fromUtf8("Apply"));

        verticalLayout->addWidget(Apply);

        Bin_color = new QCheckBox(centralwidget);
        Bin_color->setObjectName(QString::fromUtf8("Bin_color"));

        verticalLayout->addWidget(Bin_color);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        verticalLayout_4->addWidget(label_2);

        Bin_color_slider = new QSlider(centralwidget);
        Bin_color_slider->setObjectName(QString::fromUtf8("Bin_color_slider"));
        Bin_color_slider->setMaximum(255);
        Bin_color_slider->setValue(127);
        Bin_color_slider->setOrientation(Qt::Vertical);

        verticalLayout_4->addWidget(Bin_color_slider);

        Bin_color_text = new QLabel(centralwidget);
        Bin_color_text->setObjectName(QString::fromUtf8("Bin_color_text"));
        Bin_color_text->setMargin(5);

        verticalLayout_4->addWidget(Bin_color_text);


        horizontalLayout_2->addLayout(verticalLayout_4);

        verticalLayout_5 = new QVBoxLayout();
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        verticalLayout_5->addWidget(label_3);

        Scale_slider = new QSlider(centralwidget);
        Scale_slider->setObjectName(QString::fromUtf8("Scale_slider"));
        Scale_slider->setMinimum(50);
        Scale_slider->setMaximum(200);
        Scale_slider->setSingleStep(5);
        Scale_slider->setValue(100);
        Scale_slider->setOrientation(Qt::Vertical);

        verticalLayout_5->addWidget(Scale_slider);

        Scale_text = new QLabel(centralwidget);
        Scale_text->setObjectName(QString::fromUtf8("Scale_text"));
        Scale_text->setWordWrap(true);
        Scale_text->setMargin(5);

        verticalLayout_5->addWidget(Scale_text);


        horizontalLayout_2->addLayout(verticalLayout_5);


        verticalLayout->addLayout(horizontalLayout_2);


        horizontalLayout->addLayout(verticalLayout);

        line = new QFrame(centralwidget);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        horizontalLayout->addWidget(line);

        horizontalSpacer = new QSpacerItem(0, 20, QSizePolicy::Maximum, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        scrollArea = new QScrollArea(centralwidget);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        scrollArea->setMinimumSize(QSize(512, 512));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 1243, 1098));
        verticalLayout_2 = new QVBoxLayout(scrollAreaWidgetContents);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        label = new QLabel(scrollAreaWidgetContents);
        label->setObjectName(QString::fromUtf8("label"));
        label->setPixmap(QPixmap(QString::fromUtf8("../YandexDisk/\320\241\320\272\321\200\320\270\320\275\321\210\320\276\321\202\321\213/2022-03-22_17-51-24.png")));
        label->setAlignment(Qt::AlignCenter);

        verticalLayout_2->addWidget(label);

        scrollArea->setWidget(scrollAreaWidgetContents);

        horizontalLayout->addWidget(scrollArea);


        verticalLayout_3->addLayout(horizontalLayout);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 660, 21));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuFile->menuAction());
        menuFile->addAction(actionOpen);
        menuFile->addAction(actionSave);
        menuFile->addSeparator();
        menuFile->addAction(actionClose);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "Stext - Image editor", nullptr));
        actionOpen->setText(QCoreApplication::translate("MainWindow", "Open", nullptr));
        actionSave->setText(QCoreApplication::translate("MainWindow", "Save", nullptr));
        actionClose->setText(QCoreApplication::translate("MainWindow", "Close", nullptr));
        Apply->setText(QCoreApplication::translate("MainWindow", "Apply", nullptr));
        Bin_color->setText(QCoreApplication::translate("MainWindow", "bin color", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Middle", nullptr));
        Bin_color_text->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p>V: 127<br/>M: 255</p></body></html>", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "Scale", nullptr));
        Scale_text->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p>V: 100<br/>M: 200</p></body></html>", nullptr));
        label->setText(QString());
        menuFile->setTitle(QCoreApplication::translate("MainWindow", "File", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // STEXT_IMAGE_EDITOR_H
