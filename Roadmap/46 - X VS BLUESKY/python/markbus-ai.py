"""
/*
 * EJERCICIO:
 * La alternativa descentralizada a X, Bluesky, comienza a atraer
 * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 * 
 * Implementa un sistema que simule el comportamiento de estas
 * redes sociales.
 * 
 * Debes crear las siguientes operaciones:
 * - Registrar un usuario por nombre e identificador único.
 * - Un usuario puede seguir/dejar de seguir a otro.
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.   
 * - Eliminación de un post.
 * - Posibilidad de hacer like (y eliminarlo) en un post.
 * - Visualización del feed de un usuario con sus 10 publicaciones
 *   más actuales ordenadas desde la más reciente.
 * - Visualización del feed de un usuario con las 10 publicaciones
 *   más actuales de los usuarios que sigue ordenadas 
 *   desde la más reciente.
 *   
 * Cuando se visualiza un post, debe mostrarse:
 * ID de usuario, nombre de usuario, texto del post, 
 * fecha de creación y número total de likes.
 * 
 * Controla errores en duplicados o acciones no permitidas.
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**."""
import sys
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QLineEdit, QLabel, 
                            QTextEdit, QScrollArea, QMessageBox, QComboBox,
                            QStackedWidget, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor

class CustomButton(QPushButton):
    def __init__(self, text, color="#1da1f2", hover_color="#1991db"):
        super().__init__(text)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border-radius: 20px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                border: none;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
        """)

class LoginRegisterWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #15202b;
            }
            QLabel {
                color: #ffffff;
            }
            QLineEdit {
                background-color: #253341;
                color: #ffffff;
                border: 1px solid #38444d;
                border-radius: 4px;
                padding: 12px;
                font-size: 15px;
                margin: 5px 0px;
            }
            QLineEdit:focus {
                border: 1px solid #1da1f2;
                background-color: #192734;
            }
            QLineEdit::placeholder {
                color: #8899a6;
            }
            QPushButton {
                border-radius: 4px;
                padding: 12px;
                font-size: 15px;
                font-weight: bold;
            }
            QPushButton#login_btn {
                background-color: #1da1f2;
                color: white;
                border: none;
            }
            QPushButton#login_btn:hover {
                background-color: #1991db;
            }
            QPushButton#register_btn {
                background-color: transparent;
                color: #1da1f2;
                border: 1px solid #1da1f2;
            }
            QPushButton#register_btn:hover {
                background-color: rgba(29, 161, 242, 0.1);
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Container principal centrado
        main_container = QWidget()
        main_layout = QVBoxLayout(main_container)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Logo y título
        logo_container = QWidget()
        logo_layout = QVBoxLayout(logo_container)
        
        # Logo de mariposa naranja
        logo_label = QLabel("🦋")
        logo_label.setStyleSheet("""
            font-size: 48px;
            color: #f2994a;
            margin-bottom: 15px;
        """)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Título Bluesky
        title_label = QLabel("Bluesky")
        title_label.setStyleSheet("""
            font-size: 36px;
            font-weight: bold;
            color: #1da1f2;
            margin-bottom: 5px;
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Subtítulo
        subtitle = QLabel("Tu red social descentralizada")
        subtitle.setStyleSheet("""
            font-size: 16px;
            color: #8899a6;
            margin-bottom: 30px;
        """)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        logo_layout.addWidget(logo_label)
        logo_layout.addWidget(title_label)
        logo_layout.addWidget(subtitle)
        
        # Formulario
        form_container = QWidget()
        form_container.setFixedWidth(400)
        form_layout = QVBoxLayout(form_container)
        form_layout.setSpacing(15)
        
        # Campos de entrada
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Usuario')
        self.username_input.setFixedWidth(380)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Contraseña')
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedWidth(380)
        
        # Botones
        login_btn = QPushButton('Iniciar Sesión')
        login_btn.setObjectName("login_btn")
        login_btn.setFixedWidth(380)
        
        register_btn = QPushButton('Crear cuenta nueva')
        register_btn.setObjectName("register_btn")
        register_btn.setFixedWidth(380)
        
        login_btn.clicked.connect(self.login)
        register_btn.clicked.connect(self.register)
        
        # Agregar widgets al formulario
        form_layout.addWidget(self.username_input, alignment=Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(self.password_input, alignment=Qt.AlignmentFlag.AlignCenter)
        form_layout.addSpacing(10)
        form_layout.addWidget(login_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(register_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Agregar todo al layout principal
        main_layout.addWidget(logo_container)
        main_layout.addWidget(form_container)
        
        # Centrar todo en la ventana
        layout.addWidget(main_container)
        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Por favor completa todos los campos")
            return
            
        if username in self.parent.users:
            self.parent.current_user = self.parent.users[username]
            self.parent.show_main_window()
        else:
            QMessageBox.warning(self, "Error", "Usuario no encontrado")

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Por favor completa todos los campos")
            return
            
        if username in self.parent.users:
            QMessageBox.warning(self, "Error", "Este usuario ya existe")
            return
            
        user_id = len(self.parent.users) + 1
        new_user = User(username, user_id)
        self.parent.users[username] = new_user
        self.parent.current_user = new_user
        self.parent.show_main_window()

class SocialNetworkGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.users = {}
        self.posts = []
        self.current_user = None
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Crear las ventanas
        self.login_window = LoginRegisterWindow(self)
        self.main_window = QWidget()
        
        # Agregar las ventanas al stacked widget
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.main_window)
        
        # Cargar datos de ejemplo
        self.load_sample_data()
        
        self.initUI()
        # Configurar ventana en pantalla completa
        self.showMaximized()
        self.setWindowTitle('Bluesky')

    def load_sample_data(self):
        # Crear usuarios de ejemplo
        sample_users = [
            ("alice", "La exploradora del código"),
            ("bob", "Desarrollador entusiasta"),
            ("carol", "Tech lover"),
            ("david", "Python fanático"),
            ("eva", "Full-stack developer")
        ]
        
        for username, post_text in sample_users:
            user_id = len(self.users) + 1
            user = User(username, user_id)
            self.users[username] = user
            
            # Crear algunos posts para cada usuario
            post = Post(post_text, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), len(self.posts) + 1)
            post.user = user
            self.posts.append(post)
        
        # Crear algunas relaciones de seguimiento
        self.users["alice"].follow(self.users["bob"])
        self.users["alice"].follow(self.users["carol"])
        self.users["bob"].follow(self.users["alice"])
        self.users["carol"].follow(self.users["alice"])
        self.users["david"].follow(self.users["eva"])
        
        # Agregar algunos likes
        self.posts[0].likes.append(self.users["bob"])
        self.posts[0].likes.append(self.users["carol"])
        self.posts[1].likes.append(self.users["alice"])
        self.posts[2].likes.append(self.users["david"])

    def initUI(self):
        main_layout = QHBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_window.setLayout(main_layout)

        # Panel izquierdo (más compacto)
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(10, 20, 10, 20)
        left_layout.setSpacing(5)
        left_panel.setLayout(left_layout)
        left_panel.setFixedWidth(250)  # Más estrecho
        left_panel.setStyleSheet("""
            QWidget {
                background-color: #192734;
                border-right: 1px solid #38444d;
            }
        """)

        # Logo más compacto
        logo_label = QLabel("🦋")
        logo_label.setStyleSheet("""
            font-size: 32px;
            color: #1da1f2;
            padding: 10px;
        """)
        left_layout.addWidget(logo_label)

        # Botones de navegación más compactos
        nav_buttons = [
            ("🏠 Inicio", lambda: self.update_feed('all_posts')),  # Cambiado a all_posts
            ("👤 Perfil", lambda: self.update_feed('my_posts')),
            ("🔍 Explorar", lambda: None),
        ]
        
        for text, callback in nav_buttons:
            btn = QPushButton(text)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: white;
                    text-align: left;
                    padding: 12px 15px;
                    font-size: 15px;
                    border-radius: 15px;
                    margin: 2px 0px;
                }
                QPushButton:hover {
                    background-color: #253341;
                }
            """)
            btn.clicked.connect(callback)
            left_layout.addWidget(btn)

        left_layout.addStretch()

        # Panel central (más ancho)
        center_panel = QWidget()
        center_layout = QVBoxLayout()
        center_layout.setContentsMargins(10, 10, 10, 10)
        center_layout.setSpacing(10)
        center_panel.setLayout(center_layout)
        center_panel.setStyleSheet("""
            QWidget {
                background-color: #15202b;
            }
        """)

        # Área de crear post más compacta
        post_widget = QWidget()
        post_widget.setObjectName("post_widget")
        post_layout = QVBoxLayout()
        post_layout.setContentsMargins(15, 15, 15, 15)
        post_layout.setSpacing(10)
        post_widget.setLayout(post_layout)
        
        self.post_input = QTextEdit()
        self.post_input.setPlaceholderText('¿Qué está pasando?')
        self.post_input.setStyleSheet("""
            QTextEdit {
                background-color: #253341;
                border: none;
                color: white;
                font-size: 15px;
                padding: 10px;
                border-radius: 15px;
            }
        """)
        self.post_input.setFixedHeight(80)  # Más compacto
        
        post_btn = QPushButton('Publicar')
        post_btn.setStyleSheet("""
            QPushButton {
                background-color: #1da1f2;
                color: white;
                border-radius: 15px;
                padding: 8px 15px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1991db;
            }
        """)
        post_btn.setFixedWidth(80)
        post_btn.clicked.connect(self.create_post)
        
        post_layout.addWidget(self.post_input)
        post_layout.addWidget(post_btn, alignment=Qt.AlignmentFlag.AlignRight)
        center_layout.addWidget(post_widget)

        # Feed mejorado
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                background-color: #192734;
                width: 8px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background-color: #38444d;
                min-height: 30px;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        
        self.feed_widget = QWidget()
        self.feed_layout = QVBoxLayout()
        self.feed_layout.setContentsMargins(0, 0, 0, 0)
        self.feed_layout.setSpacing(5)  # Menos espacio entre posts
        self.feed_widget.setLayout(self.feed_layout)
        scroll.setWidget(self.feed_widget)
        center_layout.addWidget(scroll)

        # Panel derecho (20% del ancho)
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(20, 20, 20, 20)
        right_layout.setSpacing(10)
        right_panel.setLayout(right_layout)
        right_panel.setMinimumWidth(280)
        right_panel.setMaximumWidth(350)
        right_panel.setStyleSheet("""
            QWidget {
                background-color: #192734;
            }
        """)

        # Área de seguir usuarios
        follow_widget = QWidget()
        follow_widget.setObjectName("follow_widget")
        follow_layout = QVBoxLayout()
        follow_layout.setContentsMargins(15, 15, 15, 15)
        follow_layout.setSpacing(10)
        follow_widget.setLayout(follow_layout)
        
        follow_title = QLabel("A quién seguir")
        follow_title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: white;
            padding: 5px 0px;
        """)
        
        self.user_combo = QComboBox()
        self.user_combo.setStyleSheet("""
            QComboBox {
                background-color: #253341;
                color: white;
                border: 1px solid #38444d;
                border-radius: 15px;
                padding: 8px;
                min-height: 35px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: none;
            }
        """)
        
        follow_btn = QPushButton('Seguir/Dejar de seguir')
        follow_btn.setStyleSheet("""
            QPushButton {
                background-color: #1da1f2;
                color: white;
                border-radius: 20px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1991db;
            }
        """)
        follow_btn.clicked.connect(self.toggle_follow)
        
        follow_layout.addWidget(follow_title)
        follow_layout.addWidget(self.user_combo)
        follow_layout.addWidget(follow_btn)
        right_layout.addWidget(follow_widget)
        right_layout.addStretch()

        # Ajustar proporciones de los paneles
        main_layout.addWidget(left_panel)
        main_layout.addWidget(center_panel, 4)  # Dar más espacio al centro
        main_layout.addWidget(right_panel)

        # Establecer estilos globales
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #15202b;
            }
            QLabel {
                color: #ffffff;
            }
            QTextEdit, QLineEdit, QComboBox {
                background-color: #253341;
                color: #ffffff;
                border: 1px solid #38444d;
                border-radius: 15px;
                padding: 8px;
            }
            QWidget#post_widget, QWidget#follow_widget {
                background-color: #253341;
                border-radius: 15px;
                padding: 15px;
                margin: 10px;
            }
        """)

    def create_post(self):
        if not self.current_user:
            self.show_error("Debes iniciar sesión primero")
            return
        
        text = self.post_input.toPlainText()
        if len(text) > 200:
            self.show_error("El post no puede exceder los 200 caracteres")
            return
        
        if not text:
            self.show_error("El post no puede estar vacío")
            return
        
        new_post = Post(text, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), len(self.posts) + 1)
        new_post.user = self.current_user  # Asignar el usuario al post
        self.posts.append(new_post)
        self.post_input.clear()
        self.update_feed()
        self.show_message("Post creado exitosamente")

    def update_feed(self, feed_type='all_posts'):
        # Limpiar feed actual
        for i in reversed(range(self.feed_layout.count())): 
            widget = self.feed_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        
        if not self.current_user:
            return

        # Obtener posts según el tipo de feed
        if feed_type == 'my_posts':
            relevant_posts = [(p, p.user) for p in self.posts if p.user == self.current_user]
        elif feed_type == 'all_posts':
            # Mostrar posts propios y de usuarios seguidos
            relevant_posts = [(p, p.user) for p in self.posts 
                            if p.user == self.current_user or p.user in self.current_user.following]
        else:
            relevant_posts = [(p, p.user) for p in self.posts]

        # Ordenar por fecha
        sorted_posts = sorted(relevant_posts, key=lambda x: x[0].date, reverse=True)
        
        # Mostrar los posts
        for post, user in sorted_posts[:10]:
            post_widget = self.create_post_widget(post, user)
            self.feed_layout.addWidget(post_widget)

    def show_main_window(self):
        self.stacked_widget.setCurrentIndex(1)
        self.update_user_combo()
        self.update_feed()

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def show_message(self, message):
        QMessageBox.information(self, "Información", message)

    def update_user_combo(self):
        self.user_combo.clear()
        for username in self.users.keys():
            if username != self.current_user.username:
                self.user_combo.addItem(username)

    def toggle_follow(self):
        if not self.current_user:
            self.show_error("Debes iniciar sesión primero")
            return
        
        selected_username = self.user_combo.currentText()
        if not selected_username:
            self.show_error("Selecciona un usuario para seguir")
            return
            
        if selected_username == self.current_user.username:
            self.show_error("No puedes seguirte a ti mismo")
            return
        
        target_user = self.users[selected_username]
        
        if target_user in self.current_user.following:
            self.current_user.unfollow(target_user)
            self.show_message(f"Has dejado de seguir a {selected_username}")
        else:
            self.current_user.follow(target_user)
            self.show_message(f"Ahora sigues a {selected_username}")
        
        self.update_feed()

    def create_post_widget(self, post, user):
        post_widget = QWidget()
        post_widget.setStyleSheet("""
            QWidget {
                background-color: #1a2634;
                border: 1px solid #2f3336;
                border-radius: 0px;
                margin: 1px 0px;
            }
            QWidget:hover {
                background-color: #1e2732;
            }
            QLabel {
                color: #ffffff;
                background: transparent;
            }
            QPushButton {
                background-color: transparent;
                border: none;
                padding: 5px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: rgba(29, 161, 242, 0.1);
            }
        """)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(16, 12, 16, 12)
        main_layout.setSpacing(4)
        
        # Header
        header = QHBoxLayout()
        header.setSpacing(10)
        
        # Avatar
        avatar = QLabel("👤")
        avatar.setStyleSheet("""
            font-size: 20px;
            background-color: #253341;
            border-radius: 15px;
            padding: 5px;
            min-width: 20px;
            min-height: 20px;
        """)
        
        # Info del usuario y fecha en la misma línea
        user_info = QHBoxLayout()
        user_info.setSpacing(8)
        
        name = QLabel(user.username)
        name.setStyleSheet("font-weight: bold; font-size: 15px;")
        
        handle = QLabel(f"@{user.username}")
        handle.setStyleSheet("color: #71767b; font-size: 14px;")
        
        dot = QLabel("·")
        dot.setStyleSheet("color: #71767b; font-size: 14px; margin: 0px 4px;")
        
        date = QLabel(post.date)
        date.setStyleSheet("color: #71767b; font-size: 14px;")
        
        user_info.addWidget(name)
        user_info.addWidget(handle)
        user_info.addWidget(dot)
        user_info.addWidget(date)
        user_info.addStretch()
        
        header.addWidget(avatar)
        header.addLayout(user_info)
        
        # Contenido del post
        content = QLabel(post.text)
        content.setWordWrap(True)
        content.setStyleSheet("""
            font-size: 15px;
            color: #e7e9ea;
            padding: 0px;
            margin-left: 35px;
            line-height: 1.3;
        """)
        
        # Acciones
        actions = QHBoxLayout()
        actions.setContentsMargins(35, 0, 0, 0)
        actions.setSpacing(0)
        
        # Like con contador
        like_container = QWidget()
        like_layout = QHBoxLayout(like_container)
        like_layout.setSpacing(4)
        like_layout.setContentsMargins(0, 0, 0, 0)
        
        like_btn = QPushButton('❤️' if self.current_user not in post.likes else '💖')
        like_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                padding: 5px 8px;
                margin: 0;
            }
            QPushButton:hover {
                background-color: rgba(249, 24, 128, 0.1);
            }
        """)
        like_btn.clicked.connect(lambda: self.toggle_like(post, like_btn))
        
        likes = QLabel(str(len(post.likes)))
        likes.setStyleSheet("color: #71767b; font-size: 13px;")
        
        like_layout.addWidget(like_btn)
        like_layout.addWidget(likes)
        
        actions.addWidget(like_container)
        
        # Delete (si es el autor)
        if user == self.current_user:
            delete_container = QWidget()
            delete_layout = QHBoxLayout(delete_container)
            delete_layout.setSpacing(4)
            delete_layout.setContentsMargins(0, 0, 0, 0)
            
            delete_btn = QPushButton('🗑️')
            delete_btn.setStyleSheet("""
                QPushButton {
                    font-size: 16px;
                    padding: 5px 8px;
                    margin: 0;
                }
                QPushButton:hover {
                    background-color: rgba(244, 33, 46, 0.1);
                }
            """)
            delete_btn.clicked.connect(lambda: self.delete_post(post))
            delete_layout.addWidget(delete_btn)
            
            actions.addWidget(delete_container)
        
        actions.addStretch()
        
        # Agregar todo al layout principal
        main_layout.addLayout(header)
        main_layout.addWidget(content)
        main_layout.addLayout(actions)
        
        post_widget.setLayout(main_layout)
        return post_widget

    def toggle_like(self, post, like_btn):
        if not self.current_user:
            self.show_error("Debes iniciar sesión primero")
            return
        
        if self.current_user in post.likes:
            post.likes.remove(self.current_user)
            like_btn.setText('❤️')
        else:
            post.likes.append(self.current_user)
            like_btn.setText('💖')
        
        self.update_feed()

    def delete_post(self, post):
        if post in self.posts:
            self.posts.remove(post)
            self.update_feed()
            self.show_message("Post eliminado exitosamente")

class User:
    def __init__(self, username: str, id: int):
        self.username = username
        self.id = id
        self.followers = []
        self.following = []
        self.likes = []

    def follow(self, user):
        if user not in self.following:
            self.following.append(user)
            user.followers.append(self)

    def unfollow(self, user):
        if user in self.following:
            self.following.remove(user)
            user.followers.remove(self)

class Post:
    def __init__(self, text: str, date: str, id: int):
        self.text = text
        self.date = date
        self.id = id
        self.likes = []
        self.user = None  # Agregar referencia al usuario que creó el post

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SocialNetworkGUI()
    ex.show()
    sys.exit(app.exec())
    
