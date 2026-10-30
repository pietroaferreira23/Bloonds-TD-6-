                    self.selected_tower = tower
                    return
            self.selected_tower = None

    def activate_button(self, key: str) -> None:
        if key == "play":
            self.state = "map_select"
        elif key == "quit":
            self.running = False
        elif key == "achievements":
            self.state = "achievements"
        elif key == "back":
            self.state = "menu"
        elif key.startswith("map_"):
            index = int(key.split("_")[1])
            if index in self.profile.get("unlocked_maps", [0]):
                self.start_game(index)
        elif key.startswith("tower_"):
            self.placing = key[6:]
            self.selected_tower = None
            if self.money < TOWERS[self.placing]["price"]:
                self.message = "Voce nao tem dinheiro suficiente para esta torre."
                self.message_timer = 2
        elif key == "next_wave":
            self.start_wave()
        elif key == "pause":
            if self.state == "playing": self.state = "paused"
            elif self.state == "paused": self.state = "playing"
        elif key == "speed":
            self.speed = 1 if self.speed >= 3 else self.speed + 1
        elif key == "home" or key == "overlay_home":
            self.state = "menu"
            save_profile(self.profile)
        elif key == "upgrade":
            self.upgrade_selected()
        elif key == "sell":
            self.sell_selected()
        elif key == "target":
            tower = self.selected_tower
            if tower:
                modes = ["Mais avancado", "Mais forte", "Mais proximo"]
                tower.target_mode = modes[(modes.index(tower.target_mode) + 1) % len(modes)]
        elif key == "deselect":
            self.selected_tower = None
        elif key == "retry":
            self.start_game(self.map_index)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.VIDEORESIZE:
            self.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.handle_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
            elif event.key == pygame.K_ESCAPE:
                if self.state == "playing":
                    self.state = "paused"
                    self.placing = None
                elif self.state == "paused":
                    self.state = "playing"
                else:
                    self.state = "menu"
            elif event.key == pygame.K_SPACE and self.state == "playing":
                self.start_wave()
            elif event.key == pygame.K_p and self.state in ("playing", "paused"):
                self.state = "paused" if self.state == "playing" else "playing"
            elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3) and self.state == "playing":
                self.speed = int(event.unicode)
            elif event.key == pygame.K_F2:
                self.show_range = not self.show_range
            elif event.key == pygame.K_TAB and self.selected_tower:
                modes = ["Mais avancado", "Mais forte", "Mais proximo"]
                self.selected_tower.target_mode = modes[(modes.index(self.selected_tower.target_mode) + 1) % len(modes)]

    def render(self) -> None:
        self.canvas.fill((20, 30, 40))
        self.buttons.clear()
        if self.state == "menu":
            self.draw_menu(self.canvas)
        elif self.state == "map_select":
            self.draw_map_select(self.canvas)
        elif self.state == "achievements":
            self.draw_achievements(self.canvas)
        else:
            self.draw_game(self.canvas)
        target_w, target_h = self.screen.get_size()
        scaled = pygame.transform.smoothscale(self.canvas, (target_w, target_h))
        self.screen.blit(scaled, (0, 0))
        pygame.display.flip()

    def run(self) -> None:
        while self.running:
            dt = min(self.clock.tick(FPS) / 1000.0, .05)
            for event in pygame.event.get():
                self.handle_event(event)
            self.update(dt)
            self.render()
        save_profile(self.profile)
        pygame.quit()


def main() -> None:
    Game().run()


if __name__ == "__main__":
    main()
