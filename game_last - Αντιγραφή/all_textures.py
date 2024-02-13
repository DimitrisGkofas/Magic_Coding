import all_player as all_pl

import all_dynamic_textures as all_dy_tx

names = {
    'blank' : (0, 0, 16, 16, 1, 1, 'textures/all_10.png'),

    'theme' : (0, 0, 256, 512 ,0.5, 0.5, 'textures/theme_3.png'),

    'paper' : (256, 256, 16, 16, 1, 1, 'textures/all_10.png'),

    'sky' : (0, 0, 512, 512, 1, 1, 'textures/sky.png'),

    'menu_small' : (0, 0, 64, 64, 1, 1, 'textures/small_menu.png'),

    'menu_large' : (0, 0, 256, 512, 1, 1, 'textures/main_menu_3.png'),
    'players' : (0, 0, 240, 192, 1, 1, 'textures/best_players.png'),

    'main' : (0, 0, 96, 32, 1, 1, 'textures/main.png'),

    'level_1' : (0, 0, 96, 32, 1, 1, 'textures/level_1.png'),
    'level_2' : (0, 0, 96, 32, 1, 1, 'textures/level_2.png'),
    'level_3' : (0, 0, 96, 32, 1, 1, 'textures/level_3.png'),
    'final_level' : (0, 0, 112, 32, 1, 1, 'textures/final_level.png'),
    'locked_level' : (0, 0, 96, 64, 0.5, 0.5, 'textures/locked_level_2.png'),
    'loading_level' : (0, 0, 256, 256, 1, 1, 'textures/loading_level.png'),

    'but_det' : (0, 0, 192, 32, 1, 1, 'textures/press_icon_details.png'),
    'wasd' : (0, 0, 96, 64, 1, 1, 'textures/keys_image_2.png'),
    'arrows' : (0, 0, 96, 64, 1, 1, 'textures/arrows_image_2.png'),

    'bar' : (0, 0, 112, 16, 1, 1, 'textures/bar.png'),
    'sfx_label' : (0, 0, 96, 32, 1, 1, 'textures/sfx_label_2.png'),
    'music_label' : (0, 0, 96, 32, 1, 1, 'textures/music_label_2.png'),

    'name_input' : (0, 0, 192, 64, 1, 1, 'textures/wizards_name.png'),

    'levels' : (0, 0, 96, 32, 1, 1, 'textures/levels.png'),
    'settings' : (0, 0, 96, 32, 1, 1, 'textures/settings.png'),
    'keys' : (0, 0, 96, 32, 1, 1, 'textures/keys.png'),
    'vol_pad' : (0, 0, 32, 32, 1, 1, 'textures/volume_pad.png'),
    'sound' : (0, 0, 96, 32, 1, 1, 'textures/sound.png'),

    'help' : (0, 0, 96, 32, 1, 1, 'textures/help.png'),
    'help_details' : (0, 0, 254, 448, 0.95, 1, 'textures/help_2.png'),

    'map' : (0, 0, 1280, 608, 1, 1, 'textures/all_10.png'),
    'floor_grass' : (1280 + 9 * 32, 14 * 32, 128, 64, 1, 1, 'textures/all_10.png'),

    'mist_1' : (1280 + 1, 10 * 32 + 1, 126, 62, 1, 1, 'textures/all_10.png'),
    'mist_2' : (1280 + 4 * 32 + 1, 10 * 32 + 1, 126, 62, 1, 1, 'textures/all_10.png'),

    'book_closed' : (0, 0, 128, 128, 0.5, 0.5, 'textures/magic_book_closed_2.png'),
    'book_opened' : (0, 0, 512, 512, 1, 1, 'textures/magic_book_open_2.png'),
    'no_internet' : (0, 0, 128, 128, 0.5, 0.5, 'textures/no_internet_logo.png'),

    'game_cursor' : (0, 0, 32, 16, 1, 1, 'textures/game_cursor.png'),
    'magic_cursor' : (0, 0, 64, 64, 0.5, 0.5, 'textures/magic_cursor.png'),

    'life' : (0, 0, 128, 48, 1, 1, 'textures/life.png'),
    'magic' : (0, 0, 128, 48, 1, 1, 'textures/spell.png'),
    'time' : (0, 0, 128, 48, 1, 1, 'textures/time.png'),

    'elixir' : (0, 0, 32, 32, 1, 1, 'textures/elixir.png'),
    'clock' : (0, 0, 32, 32, 1, 1, 'textures/clock.png'),

    'loser_image' : (0, 0, 512, 512, 1, 1, 'textures/loser_image.png'),
    'winner_image' : (0, 0, 512, 512, 1, 1, 'textures/winner_image.png')
}


def collect():
    # Update all textures with player's textures too
    names.update(all_pl.names)

    # Update all textures all dynamic textures textures too
    names.update(all_dy_tx.names)