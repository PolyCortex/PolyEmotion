namespace MusicPlayerGUI
{
    partial class GraphControl
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
            this.graphSignal1 = new LiveCharts.WinForms.CartesianChart();
            this.SuspendLayout();
            // 
            // graphSignal1
            // 
            this.graphSignal1.Location = new System.Drawing.Point(52, 31);
            this.graphSignal1.Name = "graphSignal1";
            this.graphSignal1.Size = new System.Drawing.Size(732, 467);
            this.graphSignal1.TabIndex = 0;
            this.graphSignal1.Text = "cartesianChart1";
            // 
            // GraphControl
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.graphSignal1);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "GraphControl";
            this.Size = new System.Drawing.Size(805, 571);
            this.ResumeLayout(false);

        }

        #endregion

        private LiveCharts.WinForms.CartesianChart graphSignal1;
    }
}
