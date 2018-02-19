namespace MusicPlayerGUI
{
    partial class PlaylistControl
    {
        /// <summary> 
        /// Variable nécessaire au concepteur.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary> 
        /// Nettoyage des ressources utilisées.
        /// </summary>
        /// <param name="disposing">true si les ressources managées doivent être supprimées ; sinon, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Code généré par le Concepteur de composants

        /// <summary> 
        /// Méthode requise pour la prise en charge du concepteur - ne modifiez pas 
        /// le contenu de cette méthode avec l'éditeur de code.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(PlaylistControl));
            this.btnUpdatePlaylist = new System.Windows.Forms.Button();
            this.songPlaylist = new System.Windows.Forms.ListBox();
            this.mediaPlayer = new AxWMPLib.AxWindowsMediaPlayer();
            ((System.ComponentModel.ISupportInitialize)(this.mediaPlayer)).BeginInit();
            this.SuspendLayout();
            // 
            // btnUpdatePlaylist
            // 
            this.btnUpdatePlaylist.Location = new System.Drawing.Point(745, 236);
            this.btnUpdatePlaylist.Margin = new System.Windows.Forms.Padding(2);
            this.btnUpdatePlaylist.Name = "btnUpdatePlaylist";
            this.btnUpdatePlaylist.Size = new System.Drawing.Size(102, 31);
            this.btnUpdatePlaylist.TabIndex = 13;
            this.btnUpdatePlaylist.Text = "Update Playlist";
            this.btnUpdatePlaylist.UseVisualStyleBackColor = true;
            this.btnUpdatePlaylist.Click += new System.EventHandler(this.btnUpdatePlaylist_Click);
            // 
            // songPlaylist
            // 
            this.songPlaylist.FormattingEnabled = true;
            this.songPlaylist.HorizontalScrollbar = true;
            this.songPlaylist.ItemHeight = 16;
            this.songPlaylist.Location = new System.Drawing.Point(681, 43);
            this.songPlaylist.Margin = new System.Windows.Forms.Padding(2);
            this.songPlaylist.Name = "songPlaylist";
            this.songPlaylist.ScrollAlwaysVisible = true;
            this.songPlaylist.Size = new System.Drawing.Size(166, 164);
            this.songPlaylist.TabIndex = 11;
            this.songPlaylist.SelectedIndexChanged += new System.EventHandler(this.songPlaylist_SelectedIndexChanged);
            // 
            // mediaPlayer
            // 
            this.mediaPlayer.Enabled = true;
            this.mediaPlayer.Location = new System.Drawing.Point(32, 43);
            this.mediaPlayer.Margin = new System.Windows.Forms.Padding(2);
            this.mediaPlayer.Name = "mediaPlayer";
            this.mediaPlayer.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("mediaPlayer.OcxState")));
            this.mediaPlayer.Size = new System.Drawing.Size(419, 224);
            this.mediaPlayer.TabIndex = 10;
            // 
            // PlaylistControl
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.btnUpdatePlaylist);
            this.Controls.Add(this.songPlaylist);
            this.Controls.Add(this.mediaPlayer);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "PlaylistControl";
            this.Size = new System.Drawing.Size(1040, 551);
            ((System.ComponentModel.ISupportInitialize)(this.mediaPlayer)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnUpdatePlaylist;
        private System.Windows.Forms.ListBox songPlaylist;
        private AxWMPLib.AxWindowsMediaPlayer mediaPlayer;
    }
}
