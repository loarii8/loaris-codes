import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class FileToDomainConverter extends JFrame {
    private JTextField fileNameField;
    private JTextField domainLinkField;
    private JButton convertButton;
    private JButton redoButton;
    private String originalFileName;

    public FileToDomainConverter() {
        // Set up the frame
        setTitle("File to Domain Converter");
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        // Initialize components
        fileNameField = new JTextField(20);
        domainLinkField = new JTextField(20);
        domainLinkField.setEditable(false);
        convertButton = new JButton("Convert to Domain Link");
        redoButton = new JButton("Redo");
        redoButton.setEnabled(false);

        // Add action listeners
        convertButton.addActionListener(new ConvertButtonListener());
        redoButton.addActionListener(new RedoButtonListener());

        // Add components to the frame
        add(new JLabel("File Name:"));
        add(fileNameField);
        add(convertButton);
        add(new JLabel("Domain Link:"));
        add(domainLinkField);
        add(redoButton);
    }

    private class ConvertButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            originalFileName = fileNameField.getText();
            String domainLink = convertToDomainLink(originalFileName);
            domainLinkField.setText(domainLink);
            redoButton.setEnabled(true);
        }
    }

    private class RedoButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            fileNameField.setText(originalFileName);
            domainLinkField.setText("");
            redoButton.setEnabled(false);
        }
    }

    private String convertToDomainLink(String fileName) {
        // Simple conversion logic: replace spaces with dashes and append ".com"
        return fileName.replaceAll("\\s+", "-") + ".com";
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            FileToDomainConverter converter = new FileToDomainConverter();
            converter.setVisible(true);
        });
    }
}
